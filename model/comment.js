const db = require('./db')

const Comment = function(postID, date, content, name){
  this.postID = postID
  this.date = date
  this.content = content
  this.name = name
}

Comment.add = (newComment, result) => {
  db.query("INSERT INTO comments SET ?", [newComment.postID, newComment.date, newComment.content, newComment.name], (err, res)=>{
    if (err){
      console.log("error: ", err)
      result(err, null)
      return
    }

    result(null, {id: res.insertID, ...newComment})
  })
}

Comment.getComments = (id, result) => {
  db.query("SELECT * FROM comments WHERE postID = ?", -1, (err, res) => {
    if (err) {
      console.log("error: ", err)
      result(null, err)
      return
    }

    result(null, res)
  })
}

Comment.delete = (id, result) => {
  db.query('DELETE FROM comments WHERE id = ?', [id], (err, res) => {
    if(err){
      console.log("error: ", err)
      result(null, err)
      return
    }

    result(null, res)
  })
}

Comment.update = (updatedComment, result) => {
  db.query("UPDATE comments SET content = ? WHERE id = ?", [updatedComment.content, updatedComment.id], (err, res) =>{
    if(err){
      console.log("error: ", err)
      result(err, null)
      return
    }

    result(null, `Updated comment with ID: ${updatedPost.id}`)
  })
}

module.exports = Comment