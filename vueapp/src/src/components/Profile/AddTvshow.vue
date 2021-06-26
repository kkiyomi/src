<template>
  <div>
    <v-btn
     elevation="2"
     color="error"
     @click="dialogAddtv = !dialogAddtv"
     text
     small
    >
      add tv show
    </v-btn>
    <v-dialog
      elevation="4"
      v-model="dialogAddtv"
      max-width="700"
    >
      <v-card>
        <v-card-title class="headline">
          Add TVShow
        </v-card-title>
        <v-card-text>
          <v-form id="myform" ref="form" v-model="isValid">
            <v-container>
              <v-text-field
                label="Title"
                v-model="data.title"
                type="text"
                outlined
                clearable
                required
                :rules="dataRules.title"
              ></v-text-field>
              <v-textarea
                label="Description"
                v-model="data.description"
                rows="3"
                outlined
                required
                :rules="dataRules.description"
              >
              </v-textarea>
              <v-row>
                <v-col>
                  <v-file-input
                    v-model="data.image"
                    label="Image"
                    accept="image/png, image/jpeg, image/bmp"
                    prepend-icon="mdi-camera"
                    show-size
                    required
                    :rules="dataRules.image"
                  ></v-file-input>
                </v-col>
                <v-col
                  cols="3"
                >
                  <v-text-field
                    label="Year"
                    v-model="data.year"
                    outlined
                    required
                    :rules="dataRules.year"
                  >
                  </v-text-field>
                </v-col>
              </v-row>
              <v-autocomplete
                label="Genre"
                :items="genresNames"
                v-model="genre"
                filled
                dense
                auto-select-first
                chips
                deletable-chips
                small-chips
                multiple
                solo
                clearable
                outlined
                required
                :rules="dataRules.genre"
              ></v-autocomplete>
            </v-container>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <div class="mb-2">
            <v-btn @click="submit" :disabled="!isValid" class="mr-4">Submit</v-btn>
            <v-btn @click="reset" class="mr-4">clear</v-btn>
          </div>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'
export default {
  name: 'AddTvshow',

  data () {
    return {
      dialogAddtv: false,
      genre: ['Variety show'],
      isValid: true,
      dataRules: {
        title: [v => !!v || 'This Field is required'],
        description: [v => !!v || 'This Field is required'],
        year: [
          v => !!v || 'This Field is required',
          v => Number.isInteger(+v) || 'Enter a valid year'
        ],
        image: [v => !!v || 'This Field is required'],
        genre: [v => !!v || 'This Field is required'],
      },
      Resetdata: {
        title: '',
        description: '',
        year: '',
        image: null,
        genre: [],
      },
      data: {
        title: '',
        description: '',
        year: '',
        image: null,
        genre: [],
      }
    }
  },
  computed: {
    ...mapState(['genres']),
    ...mapGetters(['genresNames']),
  },
  methods: {
    ...mapActions(['addTVShow', 'getTVShowGenres']),
    reset () {
      this.data = Object.assign({}, this.Resetdata)
      this.genre = ['Variety show']
      this.$refs.form.resetValidation()
    },
    async submit () {
      this.data.genre = this.genres.filter(value => this.genre.includes(value.name)).map(value => value.id)
      const formData = new FormData()
      formData.append('title', this.data.title)
      formData.append('description', this.data.description)
      formData.append('year', this.data.year)
      formData.append('genre', this.data.genre)
      formData.append('image', this.data.image)
      await this.addTVShow(formData)
      this.reset()
    }
  },
  async created () {
    await this.getTVShowGenres()
  }
}
</script>
