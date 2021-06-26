export const SET_TVSHOWS = (state, tvshows) => {
  state.tvshows = tvshows
}

export const SET_TVSHOW_PAGINATION = (state, tvshows) => {
  state.tvshows_paginated = tvshows
}

export const SET_TVSHOW = (state, tvshow) => {
  state.tvshow = tvshow
}

export const SET_RELEASE = (state, releases) => {
  state.releases = releases
}

export const SET_TVSHOW_GENRES = (state, genres) => {
  state.genres = genres
}

export const UPDATE_READINGLIST = (state, info) => {
  if (state.selected !== info.selected) {
    state.serie_set.find(value => value.id === info.id).current_release_id = info.selected
  }
}

export const ACCOUNT_INFO = (state, account) => {
  state.account = account[0]
}

export const ACCOUNT_REGISTER = (state, data) => {
  state.token = data.token
}

export const ACCOUNT_LOGIN = (state, data) => {
  state.token = data.token
}

export const ACCOUNT_READINGLIST = (state, data) => {
  const newArray = []
  for (var i = 0; i < data.length; i++) {
    const fd = {}
    fd.id = data[i].id
    fd.cur_release_id = data[i].current_release_id
    fd.tvshow_id = data[i].tvshow.id
    fd.tvshow_title = data[i].tvshow.title
    fd.tvshow_slug = data[i].tvshow.slug
    fd.tvshow_latest_id = data[i].tvshow.latest.id
    fd.tvshow_latest_number = data[i].tvshow.latest.number
    fd.tvshow_latest_link = data[i].tvshow.latest.link
    fd.tvshow_latest_date_added = data[i].tvshow.latest.date_added
    fd.tvshow_release_id = data[i].release.id
    fd.tvshow_release_number = data[i].release.number
    fd.tvshow_release_link = data[i].release.link
    fd.tvshow_release_date_added = data[i].release.date_added
    newArray.push(fd)
  }
  state.serie_set = newArray
}

export const ALREADY_LOGGED_IN = (state, token) => {
  state.token = token
}

export const ACCOUNT_LOGOUT = (state) => {
  state.token = null
  state.account = null
  state.serie_set = []
}
