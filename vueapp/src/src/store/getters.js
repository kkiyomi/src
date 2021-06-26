export const tokenCheck = (state) => {
  return state.token
}

export const currentSerie = (state) => {
  return state.serie_set.find(value => value && state.tvshow && value.tvshow_id === state.tvshow.id)
}

export const getNumberfromId = (state, getters) => {
  return [state.releases.find(value => value && getters.currentSerie && value.id === getters.currentSerie.tvshow_release_id)]
}

export const headers = (state) => {
  return {
    headers: {
      Authorization: 'Token ' + state.token
    }
  }
}

export const genresNames = (state) => {
  return state.genres.map(value => value.name)
}
