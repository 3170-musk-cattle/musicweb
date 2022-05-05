import Vue from 'vue'
import Router from 'vue-router'
import HydrogenTest from '@/components/HydrogenUser'
import EditArtists from '@/components/EditArtists'
import AddSongsFromFile from '@/components/AddSongsFromFile'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HydrogenTest',
      component: HydrogenTest
    },
    {
      path: '/admin/artists',
      name: 'EditArtists',
      component: EditArtists
    },
    {
      path: '/admin/songs_file',
      name: 'AddSongsFromFile',
      component: AddSongsFromFile
    }
  ]
})
