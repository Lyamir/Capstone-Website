const Post = require('../model/post')
const Comment = require('../model/comment')
const Report = require('../model/report')

const routerFunctions = {
  getPosts: (req, res) => {
    Post.getAll((err, data) => {
      if(err)
        res.sendStatus(500).send({
          message: err.message || "Error"
        })
      else
        res.render('index', {
          posts: data
        })
    })
  },

  getPost: (req, res) => {
    if (!req.params){
      res.sendStatus(400).send({
        message: "Content cannot be empty"
      })
    }
    else{
      var comments = []
      Comment.getComments(req.params.id, (err, commentData) => {
        if (err)
        res.sendStatus(500).send({
          message: err.message || "An Error Occurred"
        })

        else{

          commentData.forEach(comment => {
            comments.push(JSON.parse(JSON.stringify(comment)))
          });


          Post.getPost(req.params.id, (err, postData) => {
            if (err)
            res.sendStatus(500).send({
              message: err.message || "An Error Occurred"
            })
            
            else{
              Report.addViews(req.params.id, (err, reportData) => {
                if (err)
                res.sendStatus(500).send({
                  message: err.message || "An Error Occurred"
                })
                else{
                  res.render('post', {
                    id: postData[0].id,
                    title: postData[0].title,
                    date: postData[0].date,
                    author: postData[0].author_username,
                    content: postData[0].content,
                    comments: comments
                  })
                }
              })
            }
          })
        }
      })
    }
  },

  getCreatePost: (req, res) => {
    res.render('save', {data: false})
  },

  getUpdatePost: (req, res) => {
    Post.getPost(req.params.id, (err, data) => {
      if (err)
      res.sendStatus(500).send({
        message: err.message || "An Error Occurred"
      })
      else{
        res.render('save',{
        data: true,
        id: data[0].id,
        title: data[0].title,
        author: data[0].author_username,
        content: data[0].content
      })}
    })
  },

  createPost: (req, res) => {
    if (!req.body){
      res.sendStatus(400).send({
        message: "Content cannot be empty"
      })
    }

    const post = new Post({
      title: req.body.title,
      content: req.body.content,
      date: new Date(),
      author_username: req.body.author
    })

    Post.create(post, (err, data) => {
      if (err)
        res.sendStatus(500).send({
          message: err.message || "An Error Occurred"
        })
      else res.redirect('/')
    })
  },

  deletePost: (req, res) => {
    if (!req.body){
      res.sendStatus(400).send({
        message: "Content cannot be empty"
      })
    }

    Post.delete(req.params.id, (err, data) => {
      if (err)
        res.sendStatus(500).send({
          message: err.message || "An Error Occurred"
      })
      else res.redirect('/')
    })
  },

  updatePost: (req, res) => {
    if (!req.body){
      res.sendStatus(400).send({
        message: "Content cannot be empty"
      })
    }

    const post = {
      id: req.params.id,
      title: req.body.title,
      content: req.body.content
    }

    Post.update(post, (err, data) => {
      if (err)
        res.sendStatus(500).send({
          message: err.message || "An Error Occurred"
        })
      else res.redirect('/post/' + req.params.id)
    })
  },

  editPost: (req, res) => {
    if(!req.params){
      res.sendStatus(400).send({
        message: "Content cannot be empty"
      })
    }

    Post.getPost(req.params.id, (err, data) => {
      if(err)
        res.sendStatus(500).send({
          message: err.message || "An Error Occurred"
        })
      else res.send(data[0])
    })
  }
}

module.exports = routerFunctions