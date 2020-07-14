<template>
  <div v-if="$fetchState.pending">Fetching biz #{{$route.params.id}}...</div>
  <div v-else>
    <h1>{{ biz.title }}</h1>
    <pre>{{ biz.description }}</pre>
    <p><n-link to="/">Back to bizs</n-link></p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      biz: {}
    }
  },
  async fetch() {
    const {data} = await axios.get(
      `http://localhost/api/biz/${this.$route.params.id}`
    );
    this.biz = data;
  }
}
</script>