<template>
  <div>
    <el-menu
      default-active="1"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose"
    >
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-menu"></i>
          <span>User</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="11" >Users</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group>
          <el-menu-item index="12" >Reset Password</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-headset"></i>
          <span>Songs</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="21" @click="editArtists">Add Artist</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group>
          <el-menu-item index="22">Add Album</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group>
          <el-menu-item index="23" @click="addSongs">Add Song</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'aside',
  data () {
    return {}
  },
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    },
    editArtists () {
      this.$router.push('/admin/artists')
    },
    addSongs () {
      this.$router.push('/admin/songs_file')
    }
  }
}
</script>

<style scoped>
</style>
