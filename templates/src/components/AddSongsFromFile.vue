<template>
  <div class="artist_box">
    <div>
      Song File Path: <el-input v-model="input" placeholder="File Path" style="width: 600px">File Path</el-input>
      <el-button type="success" @click="addSongsFromFile">Submit</el-button>
    </div>
    <el-table
      :data="songData"
      style="width: 800px">
      <el-table-column prop="fields.artist" label="Artist" width="100px"></el-table-column>
      <el-table-column prop="fields.name" label="Song Name" width="200px"></el-table-column>
      <el-table-column prop="fields.album" label="Album" width="200px"></el-table-column>
      <el-table-column label="Operations" width="100px" fixed="right">
        <template slot-scope="scope">
          <el-button @click="operationRow(scope.row)" type="danger" icon="el-icon-delete" circle></el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'AddSongsFromFile',
  data () {
    return {
      input: '',
      songData: []
    }
  },
  created () {
    this.showSongs()
  },
  methods: {
    showSongs () {
      this.axios.get('api/show_songs')
        .then((response) => {
          console.log(response.data.list)
          this.songData = response.data.list
        })
        .catch(function (error) { console.log(error) })
    },
    operationRow (row) {
      console.log(row.pk)
      // this.axios.get('api/delete_song', { params: { pk: row.pk } })
      //   .then((response) => {
      //     console.log(response.data.msg)
      //     this.showArtists()
      //   })
      //   .catch(function (error) { console.log(error) })
    },
    addSongsFromFile () {
      this.axios.get(
        'api/add_from_file',
        {params: {
          path: this.input
        }})
        .then((response) => {
          console.log(response.data.msg)
          this.showSongs()
        })
        .catch(function (error) { console.log(error) })
      this.input = ''
    }
  }
}
</script>

<style scoped>
.artist_box{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
</style>
