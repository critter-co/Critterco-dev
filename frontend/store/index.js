import date from '@/plugins/date-filter'
import Cookie from 'js-cookie';

const local = "http://localhost";

export const state = () => ({
  token: null
})

export const mutations = {
  setToken(state, token) {
    state.token = token
  },
  clear(state) {
    state.token = null
  }
}

export const actions = {

}

export const getters = {
  isAuthenticated(state) {
    return state.token != null
  },
}