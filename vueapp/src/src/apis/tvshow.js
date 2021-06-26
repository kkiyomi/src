import Api from './Api'

const END_POINT = 'tvshow'

export default {
  all () {
    return Api.get(END_POINT)
  },
  paginated (page) {
    return Api.get(`${END_POINT}/?page=${page}`)
  },
  detail (slug) {
    return Api.get(`${END_POINT}/${slug}/`)
  },
  releases (slug) {
    return Api.get(`release/${slug}/`)
  },
  genres () {
    return Api.get(`${END_POINT}/genre/`)
  },
  add (data) {
    return Api.post(`${END_POINT}/add/`, data)
  },
  addRelease (data) {
    return Api.post('release/add/', data)
  },
}
