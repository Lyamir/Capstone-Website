const db = require('./db')

const Post = function(title, content, date, author_username) {
    this.title = title,
    this.content = content,
    this.date = date,
    this.author_username = author_username
  }

  // TODO: Insert Post.getAll() and Post.create

Post.getPost = (id, result) => {
  db.query('SELECT * FROM posts WHERE id = ?', [id], (err, res) =>{
    if (err) {
      console.log("error: ", err)
      result(null, err)
      return
    }

    result(null, res)
  })
}

Post.delete = (id, result) => {
  db.query('DELETE FROM posts WHERE id = ?', [id], (err, res) => {
    if(err){
      console.log("error: ", err)
      result(null, err)
      return
    }

    result(null, res)
  })
}

Post.update = (updatedPost, result) => {
  db.query("UPDATE posts SET title = ?, content = ? WHERE id = ?", [updatedPost.title, updatedPost.content, updatedPost.id], (err, res) =>{
    if(err){
      console.log("error: ", err)
      result(err, null)
      return
    }

    result(null, `Updated post with ID: ${updatedPost.id}`)
  })
}



module.exports = Post
