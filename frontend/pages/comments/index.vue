<template>
  <div>
      <h1>Make a comment</h1>
      <div class="admin-auth-page">
        <div class="auth-container">
          <form @submit.prevent="makeComment">
            <AppControlInput
              v-model="content"
              type="textarea"
              placeholder="Type your comment..."
            />
            <AppControlInput v-model="biz" type="text" placeholder="biz" />
            <AppControlInput v-model="reply" type="text" placeholder="reply" />
            <AppButton type="submit">Post</AppButton>
          </form>
        </div>
      </div>

  </div>
</template>

<script>
export default {
  name: 'Comment',
  middleware: ['check-auth', 'auth'],
  data() {
    return {
      content: '',
      biz: '',
      reply: '',
    }
  },
  methods: {
    makeComment() {
      this.$store.dispatch('postComment', {
        content: this.content,
        biz: this.biz,
        reply: this.reply,
      })
    },
  },
}
</script>

<style scoped>
h1 {
  text-align: center;
  text-decoration: bold;
  padding: 0px 0px 20px 0px;
}
.admin-auth-page {
  padding: 20px;
}

.auth-container {
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 2px #ccc;
  width: 300px;
  margin: auto;
  padding: 10px;
  box-sizing: border-box;
}
</style>
