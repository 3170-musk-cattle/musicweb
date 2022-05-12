<template>
  <div>
    <Tables/>
    <chart-view/>
  </div>
</template>

<script lang="js">
import Tables from '@/views/Tables'
import ChartView from "@/views/ChartView";
export default {
  name: 'OxygenTest',
  components: {ChartView, Tables},
  data() {
    return {
      name: 'jdr'
    }
  }
}
</script>
