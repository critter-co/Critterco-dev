import SecureLs from 'secure-ls'
import createPersistedState from 'vuex-persistedstate'

var ls = new SecureLs({ isCompression: false })

export default ({ store }) => {
  window.onNuxtReady(() => {
    createPersistedState({
      key: 'inf',
      paths: ['user.user'],
      storage: {
        getItem: (key) => ls.get(key),
        setItem: (key, value) => ls.set(key, value),
        removeItem: (key) => ls.remove(key),
      }
    })(store)
  })
}