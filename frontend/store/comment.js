const local = "http://localhost";

export const state = () => {

}

export const mutations = {}

export const actions =
{
  postComment(vuexContext, commentData) {
    let commentUrl = `${local}/api/comments/`
    return this.$axios.$post(commentUrl, {
      content: commentData.content,
      biz: commentData.biz,
      reply: commentData.reply
    }).then(result => {
    }).catch(e => {
      console.log(e)
    })
  },
}

export const getters = {}