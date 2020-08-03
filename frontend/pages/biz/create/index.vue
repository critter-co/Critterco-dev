<template>
  <div>
    <h1>Create your Business</h1>
      <form  class="new-post-form" @submit.prevent="onCreate">
        <AppControlInput v-model="title">Title</AppControlInput>
        <AppControlInput control-type="textarea" v-model="description"
          >Description</AppControlInput
        >
        <AppControlInput control-type="textarea" v-model="address"
          >Address</AppControlInput
        >
        <AppControlInput v-model="city">City</AppControlInput>
        <AppControlInput v-model="phone">Phone</AppControlInput>
        <AppControlInput v-model="phone2">Phone 2</AppControlInput>
        <!-- <AppControlInput>Gallery</AppControlInput> -->
        <AppControlInput v-model="website">Website</AppControlInput>
        <AppControlInput v-model="instagram">Instagram</AppControlInput>
        <AppControlInput v-model="telegram">Telegram</AppControlInput>
        <div id="map-wrap" style="height: 70vh; width: 200vh;">
          <client-only>
            <button type="button" v-on:click="show">Click to see the indicator</button>
              <l-map
                ref="map"
                @ready="add()"
                :zoom="20"
                :center="[35.8351372, 51.0103949]"
              >
                <l-tile-layer
                  url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
                ></l-tile-layer>
                <l-marker
                  ref="marker"
                  :visible="visible"
                  :draggable="true"
                  :lat-lng="markers"
                ></l-marker>
              </l-map>
          </client-only>
        </div>
        <AppButton type="submit">Create</AppButton>
        <AppButton
          type="button"
          style="margin-left: 10px;"
          btn-style="cancel"
          @click="onCancel"
          >Cancel</AppButton
        >
      </form>
  </div>
</template>

<script>
import Vue from 'vue'
export default {
  name: 'CreatingBiz',
  components: {},
  data() {
    return {
      visible: false,
      markers: [35.8351372, 51.0103949],
      newLoc: [],
      title: '',
      description: '',
      address: '',
      city: '',
      phone: '',
      phone2: '',
      // gallery: '',
      website: '',
      instagram: '',
      telegram: ''
    }
  },
  methods: {
    add: async function(){
       await this.$refs.marker.mapObject.on('dragend', function (ev) {
       var marker = ev.target // you could also simply access the marker through the closure
       const result = marker.getLatLng() // but using the passed ev is cleaner
      //  console.log(result)
      })
        
    },
    show: function (){
      this.visible = true
    },
    onCreate(){
      const loc = this.$refs.marker.mapObject
      this.newLoc = loc._latlng
      this.$store.dispatch('biz/createBiz', {
        title: this.title,
        description: this.description,
        address: this.address,
        city: this.city,
        phone: this.phone,
        phone2: this.phone2,
        website: this.website,
        instagram: this.instagram,
        telegram: this.telegram,
        loc: this.newLoc

      }).then(()=>{
      })
    },
    onCancel(){
      this.$router.push('/');
    }
  },
}
</script>

<style scoped>
.new-post-form {
  width: 90%;
  margin: 20px auto;
}

@media (min-width: 768px) {
  .new-post-form {
    width: 500px;
  }
}
</style>
