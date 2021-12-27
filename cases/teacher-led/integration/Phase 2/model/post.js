const db = require('./db')

const Post = function(title, content, date, author_username) {
    this.title = title,
    this.content = content,
    this.date = date,
    this.author_username = author_username
  }

  //Programmer 1:Insert Post.create here

Post.getAll = result => {
    db.query("SELECT * FROM posts", (err, res) => {
      if (err) {
        console.log("error: ", err)
        result(null, err)
        return
      }
  
      result(null, res)
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

//Programmer 2:Insert Post.delete here

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

// TODO Phase2: Creation of Post.create and Post.delete

module.exports = Post
