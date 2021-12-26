const db = require('./db')

const Report = function(postID, views, numComments){
  this.postID = postID,
  this.views = views,
  this.numComments = numComments
}

//TODO: Add getReports() here:

Report.addViews = (id, result) => {
  db.query("UPDATE reports SET views = views + 1 WHERE postID = ?", [id], (err, res) => {
    if (err) {
      console.log("error: ", err)
      result(null, err)
      return
    }

    result(null, res)
  })
}

Report.addComment = (id, result) => {
    db.query("UPDATE reports SET numComments = numComments + 1 WHERE postID = ?", [id], (err, res) => {
      if (err) {
        console.log("error: ", err)
        result(null, err)
        return
      }
  
      result(null, res)
    })
}

module.exports = Report