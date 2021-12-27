const db = require('./db')

const Post = function(title, content, date, author_username) {
    this.title = title,
    this.content = content,
    this.date = date,
    this.author_username = author_username
  }


Post.create = (newPost, result) => {
  db.query("INSERT INTO posts SET ?", [newPost.title, newPost.content, newPost.date, newPost.author_username], (err, res) =>{
    if(err){
      console.log("error: ", err)
      result(err, null)
      return
    }

    result(null, {id: res.insertID, ...newPost})
  })
}

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

// TODO: Insert Post.getAll() here:

module.exports = Post
