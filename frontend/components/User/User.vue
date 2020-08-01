<template>
  <form @submit.prevent="onSave">
    <AppControlInput v-model="updatedUser[1]">FirstName</AppControlInput>

    <AppControlInput v-model="updatedUser[2]">Lastname</AppControlInput>

    <AppControlInput v-model="updatedUser[0]">Email</AppControlInput>

    <AppControlInput v-model="updatedUser[3]">Username</AppControlInput>

    <AppControlInput v-model="updatedUser[4]">phone</AppControlInput>

    <AppButton type="submit">Save</AppButton>

    <AppButton type="button" style="margin-left: 10px" btn-style="cancel" @click="onCancel">Cancel</AppButton>
  </form>
</template>

<script>
export default {
  name: 'User',
  props: {
    user: {
      type: Array,
      required: false
    }
  },
  data() {
    return {
      updatedUser: this.user
        ? { ...this.user }
        : {
            [1]: "",
            [2]: "",
            [3]: "",
            [0]: "",
            [4]: ""
          }
    };
  },
  methods: {
    onSave() {
      //Save the user
      this.$emit("submit", this.updatedUser);
    },
    onCancel() {
      // NAvigate Back
      this.$router.push("/");
    }
  }
};
</script>