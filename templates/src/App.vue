<template>
  <div id="app">
    <el-container>
      <el-header><app-header/></el-header>
      <el-container>
        <el-aside width="200px" v-if="side_show"><app-aside></app-aside></el-aside>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import Header from '@/components/header'
import Footer from '@/components/footer'
import aside from '@/components/aside'
export default {
  name: 'App',
  data () {
    return {
      header_show: true,
      footer_show: true,
      side_show: true
    }
  },
  components: {
    'app-aside': aside,
    'app-header': Header,
    'app-footer': Footer
  },
  methods: {
    header: function (bool) {
      this.header_show = bool
    },
    footer: function (bool) {
      this.footer_show = bool
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: white;
}
.el-header{
  position: relative;
  width: 100%;
  height: 120px;
  line-height: 60px;
  color: cornsilk;
  background-color: steelblue;
}
/*.el-header, .el-footer {*/
/*  background-color: #B3C0D1;*/
/*  color: #333;*/
/*  text-align: center;*/
/*  line-height: 60px;*/
/*}*/

.el-aside {
  position: relative;
  background-color: gray;
  color: #333;
  text-align: center;
  height: auto;
}

/*.el-main {*/
/*  background-color: #E9EEF3;*/
/*  color: #333;*/
/*  text-align: center;*/
/*  line-height: 160px;*/
/*}*/

/*.el-container:nth-child(5) .el-aside,*/
/*.el-container:nth-child(6) .el-aside {*/
/*  line-height: 260px;*/
/*}*/

/*.el-container:nth-child(7) .el-aside {*/
/*  line-height: 320px;*/
/*}*/
</style>
