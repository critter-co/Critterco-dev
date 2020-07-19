import Vuex from 'vuex';
import date from '@/plugins/date-filter'
import Cookie from 'js-cookie';


const createStore = () => {
  return new Vuex.Store({
    state: {
      token: null,
      refreshToken: null,
      user: [],
      biz: [],
    },
    mutations: {
      getBiz(state, bizes) {
        state.biz = bizes
      },
      addBiz(state, biz) {
        state.biz.push(biz)
      },
      setToken(state, token) {
        state.token = token
      },
      setRefreshToken(state, refToken) {
        if (process.client) {
          state.refreshToken = JSON.stringify(localStorage.getItem("RsagT"))
        }
        state.refreshToken = refToken
      },
      clearToken(state) {
        state.token = null,
          state.refreshToken = null,
          state.user.length = 0
      },
      addUserInfo(state, info) {
        state.user = (info)
      },
    },
    actions: {
      // nuxtServerInit(vuexContext, context) {
      //   return context.app.$axios.$get('localhost/api/biz')
      //     .then(res => {
      //       const bizArray = [];

      //       for (const key in res.data) {
      //         bizArray.push({...res.data[key] })
      //         if (bizArray.length === 2) return
      //       }
      //       vuexContext.commit('getBiz', bizArray)
      //     }).catch(e => console.log(e))
      // },
      signingup(vuexContext, authData) {
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

          }).then(result => {
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
        }).then(async result => {
          await vuexContext.commit('setToken', result.access)
          vuexContext.commit('setRefreshToken', result.refresh)
          this.$axios.setHeader('Authorization', `Bearer ${result.access}`)
          Cookie.set('CAT', result.access, { expires: new Date(new Date().getTime() + 5 * 60 * 1000) })
          Cookie.set('CATExp', date(new Date().getTime() + 5 * 60 * 1000), { expires: new Date(new Date().getTime() + 5 * 60 * 1000) })
          localStorage.setItem('RsagT', JSON.stringify(result.refresh))
          localStorage.setItem('RsagTExp', new Date().getTime() + 86400000)
          vuexContext.dispatch('gettingInfo', authInfo.email)

        }).catch(e => {
          console.log(e)
        })
      },
      async gettingInfo(vuexContext, email) {
        console.log('Getting info...')
        return await this.$axios.get('http://localhost/api/user/me', {
          email: email.email
        }).then(res => {
          const info = [];
          for (const key in res.data) {
            info.push(res.data[key])
          }

          vuexContext.commit('addUserInfo', info)
        }).catch(e => {
          console.log(e)
        })
      },
      checkAuth(vuexContext, req) {
        let token;
        let tokenRef;
        let expirationDate;
        if (req) {
          if (!req.headers.cookie) {
            return
          }
          const cat = req.headers.cookie.split(';').find(c => c.trim().startsWith('CAT='));
          if (!cat) {
            return
          }
          token = cat.split('=')[1];
          expirationDate = req.headers.cookie.split(';').find(c => c.trim().startsWith('CATExp=')).split('=')[1];
          if (new Date().getTime() > +expirationDate || !token) {
            return
          }
        }
        else {
          tokenRef = localStorage.getItem("RsagT");
          expirationDate = localStorage.getItem("RsagTExp");
          if (new Date().getTime() < +expirationDate && tokenRef) {
            console.log("refreshing Token: ", tokenRef)
            return this.$axios.$post("http://localhost/api/token/refresh/", {
              refresh: tokenRef
            }).then(async result => {
              await this.$axios.setHeader('Authorization', `Bearer ${result.access}`)
              token = result.access
              Cookie.set('CAT', result.access, { expires: new Date(new Date().getTime() + 5 * 60 * 1000) })
              Cookie.set('CATExp', date(new Date().getTime() + 5 * 60 * 1000))
              console.log("Authorized by refresh")
            }).catch(e => {
              console.log(e)
            })
          }
        }
        if (new Date().getTime() > +expirationDate || !token) {
          console.log("No token or invalid token");
          vuexContext.dispatch("logout");
          return;
        }
        vuexContext.commit("setToken", token)
        vuexContext.commit("setRefreshToken", tokenRef)

      },
      postComment(vuexContext, commentData) {
        let commentUrl = "http://localhost/api/comments/"
        return this.$axios.$post(commentUrl, {
          content: commentData.content,
          biz: commentData.biz,
          reply: commentData.reply
        }).then(result => {
        }).catch(e => {
          console.log(e)
        })
      },
      logout(vuexContext) {
        vuexContext.commit('clearToken');
        Cookie.remove('CAT');
        Cookie.remove('CATExp');
        if (process.client) {
          localStorage.removeItem('RsagT');
          localStorage.removeItem('RsagTExp');
        }
      }
    },
    getters: {
      isAuthenticated(state) {
        return state.token != null
      },
      refreshAvailable(state) {
        return state.refreshToken != null
      },
      loadedBizs(state) {
        return state.biz
      },
      userInfo(state) {
        return state.user.length > 0
      },
      userData(state) {
        return state.user
      },
    },
  })
}

export default createStore;