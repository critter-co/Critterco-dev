<template>
  <div>
    <h1>Welcome to Critter</h1>
    <div>
      <Map></Map>
    </div>
  </div>
</template>

<script>
import Map from '@/components/Map/Map'
export default {
  name: 'Home',
  components: {
    Map,
  },
}
</script>

<style scoped>
h1 {
  text-align: center;
}
</style>
