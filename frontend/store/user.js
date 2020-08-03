import Cookie from 'js-cookie';

const local = "http://localhost";

export const state = () => ({
  user: [],
})

export const mutations = {
  addUserInfo(state, info) {
    state.user = info
  },
  clearUser(state) {
    state.user.length = 0
  },
  updateUser(state, name) {
    state.user = name
  }
}

export const actions = {
  async gettingInfo(vuexContext, email) {
    console.log('Getting info...')
    return await this.$axios.get(`${local}/api/user/me`, {
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

  updateUser(vuexContext, updateInfo) {
    const auth = Cookie.get('CAT');
    return this.$axios.$patch(`${local}/api/user/me`, {
      first_name: updateInfo.first_name,
      last_name: updateInfo.last_name,
      email: updateInfo.email,
      username: updateInfo.username,
      phone: updateInfo.phone
    }, { headers: { 'Authorization': `Bearer ${auth}` } }).then(res => {
      let updated = [];
      vuexContext.commit("addUserInfo", updated)
      for (const key in res) {
        updated.push(res[key])
      }
      vuexContext.commit('addUserInfo', updated)
    }).catch(e => {
      console.log(e)
    })
  },
  logout(vuexContext) {
    vuexContext.commit('clearUser')
  }
}

export const getters = {
  userInfo(state) {
    return state.user.length > 0
  },
  userData(state) {
    return state.user
  },
}