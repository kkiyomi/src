import Api from './Api'
import store from '../store'

const END_POINT = 'account'

export default {
  info() {
    return Api.get(`${END_POINT}/user/`, store.getters.headers)
  },
  register(data) {
    return Api.post(`${END_POINT}/register/`, data)
  },
  login(data) {
    return Api.post(`${END_POINT}/login/`, data)
  },
  readinglist(id) {
    return Api.get(`${END_POINT}/readinglist/${id}/`)
  },
  addReadinglist() {
    return Api.get(`${END_POINT}/add/`, store.getters.headers)
  },
  serieAdd(data) {
    return Api.post(`${END_POINT}/addserie/`, data, store.getters.headers)
  },
  serieUpdate(data) {
    return Api.put(`${END_POINT}/serie/${data.id}/`, data.data, store.getters.headers)
  },
  serieDelete(id) {
    return Api.delete(`${END_POINT}/serie/${id}/`, store.getters.headers)
  },
}
