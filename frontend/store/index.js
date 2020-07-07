import Vuex from 'vuex';
// import Cookie from 'js-cookie';


const createStore = () => {
  return new Vuex.Store({
    state: {
      token: null,
    },
    mutations: {
      setToken(state, token) {
        state.token = token
      },
      clearToken(state) {
        state.token = null
      }
    },
    actions: {
      async signingup(vuexContext, authData) {
        let authUrl =
          "http://localhost/api/user/create/";
        return this.$axios
          .$post(authUrl, {
            first_name: authData.first_name,
            last_name: authData.last_name,
            email: authData.email,
            password: authData.password,
            username: authData.username,
            name: authData.name,
            phone: authData.phone,
            returnSecureToken: true

          }).then(result => {
            console.log(result);
          }).catch(e => console.log(e));
      },
      activate(vuexContext, authCode) {
        let activateUrl = "http://localhost/api/user/confirm"
        return this.$axios.$post(activateUrl, {
          code: authCode.code
        }).then(result => {
          console.log(result)
        }).catch(e => {
          console.log(e)
        })
      },
      accessToken(vuexContext, authInfo) {
        let accessUrl = "http://localhost/api/token/"
        return this.$axios.$post(accessUrl, {
          email: authInfo.email,
          password: authInfo.password,
          returnSecureToken: true
        }).then(async result => {
          await vuexContext.commit('setToken', result.access)
          this.$axios.setHeader('Authorization', `Bearer ${result.access}`)
        }).catch(e => {
          console.log(e)
        })
      },
      postComment(vuexContext, commentData) {
        let commentUrl = "http://localhost/api/comments/"
        return this.$axios.$post(commentUrl, {
          content: commentData.content,
          biz: commentData.biz,
          reply: commentData.reply
        }).then(result => {
          console.log(result)
        }).catch(e => {
          console.log(e)
        })
      }
    },
    getters: {
      isAuthenticated(state) {
        return state.token != null
      }
    },
  })
}

export default createStore;