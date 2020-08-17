<template>
  <div>
    <div id="map"></div>
  </div>
</template>

<script>
import axios from 'axios'
import Mapbox from 'mapbox-gl'
export default {
  name: 'biz',
  data() {
    return {
      access_token: this.$config.mapbox,
      map: {},
      bizs: [],
      myLat: '',
      myLng: '',
    }
  },
  mounted() {
    this.createMap()
    this.getBiz()
  },
  methods: {
    createMap() {
      ;(Mapbox.accessToken = this.access_token),
        (this.map = new Mapbox.Map({
          container: 'map',
          style: 'mapbox://styles/vturnus/ckdq0q5iw0qh81io84mszhpww',
          zoom: 15,
        }))
    },
    async getBiz() {
      await this.$getLocation({
        enableHighAccuracy: true,
      })
        .then((coordinates) => {
          this.myLat = coordinates.lat
          this.myLng = coordinates.lng
        })
        .catch((e) => {
          console.log(e.message)
        })
      const { data } = await axios.get(
        `http://localhost/api/biz/?dist=4000&point=${this.myLng},${this.myLat}&format=json`
      )

      // `bizs` has to be declared in data()
      const bounds = new Mapbox.LngLatBounds()
      data.forEach((loc) => {
        const el = document.createElement('div')
        el.className = 'marker'
        new Mapbox.Marker({
          element: el,
          anchor: 'bottom',
        })
          .setLngLat({
            lng: loc.location.coordinates[0],
            lat: loc.location.coordinates[1],
          })
          .addTo(this.map)

        new Mapbox.Popup({
          offset: 5,
        })
          .setLngLat({
            lng: loc.location.coordinates[0],
            lat: loc.location.coordinates[1],
          })
          .setHTML(
            `<p><a href="/biz/${loc.id}" target=_blank title="Opens in a new window">${loc.title}:</a> ${loc.description}</p>`
          )
          .addTo(this.map)
        bounds.extend(loc.location.coordinates)
      })
      this.map.fitBounds(bounds, {
        padding: {
          top: 50,
          bottom: 50,
          left: 0,
          right: 0,
        },
      })
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
