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
      async signingup(vuexContext, authData, state) {
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
            vuexContext.commit('setToken', result.idToken)
            localStorage.setItem('token', result.idToken)
            console.log(result);
          }).catch(e => console.log(e));
      },
      activate(authCode) {
        let activateUrl = "http://localhost/api/user/confirm"
        return this.$axios.$post(activateUrl, {
          code: authCode.code
        }).then(result => {
          console.log(result)
        }).catch(e => {
          console.log(e)
        })
      }
    },
    getters: {

    },
  })
}

export default createStore;