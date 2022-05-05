<template>
  <div class="box">
    <div>
      <el-input v-model="input_name" placeholder="User Name" style="width: 300px"></el-input>
      <br>
      <el-input v-model="input_email" placeholder="Email Address" style="width: 300px"></el-input>
      <br>
      <el-input v-model="input_passwd" placeholder="Password" style="width: 300px"></el-input>
      <br>
      <el-button type="success" @click="addUser">Register</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HydrogenTest',
  data () {
    return {
      input_name: '',
      input_email: '',
      input_passwd: '',
      tableData: []
    }
  },
  created () {
    this.showUser()
  },
  methods: {
    showUser () {
      this.axios.get('http://localhost:8000/show_users/')
        .then((response) => {
          console.log(response.data.list)
          this.tableData = response.data.list
        })
        .catch(function (error) { console.log(error) })
    },
    addUser () {
      this.axios.get(
        'http://localhost:8000/add_user/',
        {params: {
            user_name: this.input_name,
            email: this.input_email,
            password: this.input_passwd
          }})
        .then((response) => {
          console.log(response.data.msg)
          this.showUser()
        })
        .catch(function (error) { console.log(error) })
    }
  }
}
</script>
<style scoped>
.box{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
</style>
