<template>
  <v-navigation-drawer
    class="deep-purple accent-4"
    dark
    width="100%"
    v-model="drawerToggle"
    absolute
  >
    <v-list>
      <v-list-item
        v-for="item in items"
        :key="item.title"
        link
      >
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  data () {
    return {
      items: [
        { title: 'Dashboard', icon: 'fas fa-lock' },
        { title: 'Account', icon: 'fas fa-lock' },
        { title: 'Admin', icon: 'fas fa-lock' }
      ]
    }
  },
  computed: {
    drawerToggle: {
      get() {
        return this.$store.state.drawer.drawerToggle
      },
      set() {
        return
      }
    }
  }
}
</script>

<style scoped>

</style>
