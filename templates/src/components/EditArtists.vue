<template>
  <div class="artist_box">
    <div>
      New Artist  <el-input v-model="input" placeholder="Artist Name" style="width: 200px">Artist Name</el-input>
      <el-button type="success" @click="addArtist">Submit</el-button>
    </div>
    <el-table
      :data="artistData"
      style="width: 400px">
      <el-table-column prop="fields.name" label="Artist Name" width="200px"></el-table-column>
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
  name: 'EditArtists',
  data () {
    return {
      input: '',
      artistData: []
    }
  },
  created () {
    this.showArtists()
  },
  methods: {
    showArtists () {
      this.axios.get('api/show_artists')
        .then((response) => {
          console.log(response.data.list)
          this.artistData = response.data.list
        })
        .catch(function (error) { console.log(error) })
    },
    operationRow (row) {
      console.log(row.pk)
      this.axios.get('api/delete_artist', { params: { pk: row.fields.name } })
        .then((response) => {
          console.log(response.data.msg)
          this.showArtists()
        })
        .catch(function (error) { console.log(error) })
    },
    addArtist () {
      this.axios.get(
        'api/add_artist',
        {params: {
          name: this.input
        }})
        .then((response) => {
          console.log(response.data.msg)
          this.showArtists()
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
