<template>
  <div v-if="toggleHeader">
    <v-app-bar flat fixed>
      <v-app-bar-nav-icon @click="turnonDrawer"></v-app-bar-nav-icon>
    </v-app-bar>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'

export default {
  computed: {
    ...mapState({
      toggleHeader: state => state.toggle.headerShow,
    }),
  },
  methods: {
    ...mapMutations('toggle', ['toggleNavDrawer']),
    turnonDrawer() {
      this.toggleNavDrawer(true)
    }
  }
}
</script>