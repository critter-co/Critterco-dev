import date from '@/plugins/date-filter'
import Cookie from 'js-cookie';

const local = "http://localhost";

export const state = () => ({
  token: null,
  refreshToken: null
})

export const mutations = {
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
      state.refreshToken = null
  },
}

export const actions = {
  signingup(vuexContext, authData) {
    let authUrl = `${local}/api/user/create/`;
    return this.$axios
      .$post(authUrl, {
        first_name: authData.first_name,
        last_name: authData.last_name,
        email: authData.email,
        password: authData.password,
        username: authData.username,
        phone: authData.phone,

      }).then(result => {
      }).catch(e => console.log(e));
  },
  activate(vuexContext, authCode) {
    let activateUrl = `${local}/api/user/confirm`
    return this.$axios.$post(activateUrl, {
      code: authCode.code
    }).then(result => {
    }).catch(e => {
      console.log(e)
    })
  },
  accessToken(vuexContext, authInfo) {
    let accessUrl = `${local}/api/token/`
    return this.$axios.$post(accessUrl, {
      email: authInfo.email,
      password: authInfo.password,
    }).then(async result => {
      await vuexContext.commit('setToken', result.access)
      await vuexContext.commit('setToken', result.access, { root: true })
      vuexContext.commit('setRefreshToken', result.refresh)
      this.$axios.setHeader('Authorization', `Bearer ${result.access}`)
      Cookie.set('CAT', result.access, { expires: new Date(new Date().getTime() + 5 * 60 * 1000) })
      Cookie.set('CATExp', date(new Date().getTime() + 5 * 60 * 1000), { expires: new Date(new Date().getTime() + 5 * 60 * 1000) })
      localStorage.setItem('RsagT', result.refresh)
      localStorage.setItem('RsagTExp', new Date().getTime() + 86400000)
      vuexContext.dispatch('user/gettingInfo', authInfo.email, { root: true })

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

        return this.$axios.$post(`${local}/api/token/refresh/`, {
          refresh: tokenRef
        }).then(async result => {
          await this.$axios.setHeader('Authorization', `Bearer ${result.access}`)
          token = result.access
          Cookie.set('CAT', result.access, { expires: new Date(new Date().getTime() + 5 * 60 * 1000) })
          Cookie.set('CATExp', date(new Date().getTime() + 5 * 60 * 1000))
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
    vuexContext.commit("setToken", token, { root: true })
    vuexContext.commit("setRefreshToken", tokenRef)

  },
  logout(vuexContext) {
    vuexContext.commit('clearToken');
    vuexContext.commit('clear', null, { root: true });
    Cookie.remove('CAT');
    Cookie.remove('CATExp');
    if (process.client) {
      localStorage.removeItem('RsagT');
      localStorage.removeItem('RsagTExp');
      localStorage.removeItem('inf')
    }
  }
}

export const getters = {
  isAuthenticated(state) {
    return state.token != null
  },
  refreshAvailable(state) {
    return state.refreshToken != null
  },
}