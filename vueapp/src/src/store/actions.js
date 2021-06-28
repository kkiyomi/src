import Vue from 'vue'
import tvshow from '../apis/tvshow'
import account from '../apis/account'

export const getTVShowList = ({ commit }) => {
  tvshow.all().then(response => {
    commit('SET_TVSHOWS', response.data)
  })
}

export const getTVShowPagination = ({ commit }, page) => {
  tvshow.paginated(page).then(response => {
    commit('SET_TVSHOW_PAGINATION', response.data)
  })
}

export const getTVShowDetail = ({ commit }, slug) => {
  tvshow.detail(slug).then(response => {
    commit('SET_TVSHOW', response.data)
  })
}

export const getTVShowGenres = async ({ commit }) => {
  await tvshow.genres().then(response => {
    commit('SET_TVSHOW_GENRES', response.data)
  })
}

export const getReleaseList = async ({ commit }, id) => {
  await tvshow.releases(id).then(response => {
    commit('SET_RELEASE', response.data)
  })
}

export const addTVShow = async ({ commit }, data) => {
  await tvshow.add(data).then(response => {
  })
}

export const UpdateSerie = async ({ commit }, info) => {
  await account.serieUpdate({
    id: info.id,
    data: {
      current_release_id: info.selected,
    }
  }).then(response => {
    commit('UPDATE_READINGLIST', info)
  })
}

export const DeleteSerieFromReadingList = async ({ commit }, id) => {
  await account.serieDelete(id)
}

export const AddSerieToReadingList = async ({ commit }, data) => {
  await account.serieAdd(data)
}

export const getAccountInfo = async ({ commit }) => {
  await account.info().then(response => {
    commit('ACCOUNT_INFO', response.data)
  })
}

export const AccountRegister = async ({ commit }, info) => {
  await account.register(info).then(response => {
    commit('ACCOUNT_REGISTER', response.data)
    Vue.prototype.$cookies.set('at', response.data.token)
  })
}

export const AccountLogin = async ({ commit }, info) => {
  await account.login(info).then(response => {
    commit('ACCOUNT_LOGIN', response.data)
    Vue.prototype.$cookies.set('at', response.data.token, info.cookies_setting)
  })
}

export const AccountReadinglist = async ({ commit }, id) => {
  await account.readinglist(id).then(response => {
    commit('ACCOUNT_READINGLIST', response.data)
  })
}

export const AddReadinglist = async ({ commit }) => {
  await account.addReadinglist()
}

export const AlreadyLoggedIn = ({ commit }, token) => {
  commit('ALREADY_LOGGED_IN', token)
}

export const AccountLogout = ({ commit }) => {
  Vue.prototype.$cookies.remove('at')
  commit('ACCOUNT_LOGOUT')
}
