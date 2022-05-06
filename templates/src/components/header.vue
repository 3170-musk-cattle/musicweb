<template>
  <el-row :gutter="20">
    <el-col :span="2">
      <el-button @click="expand_side" icon="el-icon-toilet-paper" circle></el-button>
    </el-col>
    <el-col :span="6">MCCMS</el-col>
    <el-col :span="6"></el-col>
    <el-col :span="6"></el-col>
  </el-row>
</template>

<script>
export default {
  name: 'app-header',
  data () {
    return {
      toggle_: true
    }
  },
  methods: {
    expand_side () {
      this.toggle_ = !this.toggle_
      return this.toggle_
    }
  },
  created () {
  }
}
</script>

<style scoped>
  .head_title{
    color: #2c3e50;
    text-align: center;
  }
</style>
