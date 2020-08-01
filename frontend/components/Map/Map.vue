<template>
  <div>
    <div id="map"></div>
  </div>
</template>

<script>
import Mapbox from 'mapbox-gl'
export default {
  name: 'Map',
  data() {
    return {
      access_token: this.$config.mapbox,
      map: {},
    }
  },
  mounted() {
    this.createMap()
  },
  methods: {
    createMap() {
      ;(Mapbox.accessToken = this.access_token),
        (this.map = new Mapbox.Map({
          container: 'map',
          style: 'mapbox://styles/mapbox/streets-v11',
          zoom: 15,
          center: [51.0104916, 35.8351016],
        }))
    },
  },
}
</script>
<style scoped>
#map {
  padding: 50px 50px 50px 50px;
  width: 80%;
  height: 60vh;
}
</style>
