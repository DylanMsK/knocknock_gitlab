<template>
  <div v-if="toggleNavDrawer">
    <!-- App bar -->
    <v-app-bar flat>
      <v-app-bar-nav-icon @click="drawer=!drawer"></v-app-bar-nav-icon>
    </v-app-bar>

    <!-- Navigation Drawer -->
    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
      width="100%"
    >
      <v-list-item>
        <v-btn
          icon
          @click="drawer=!drawer"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn
          icon
          class="mx-3">
          <v-icon>mdi-settings-outline</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>mdi-bell-outline</v-icon>
        </v-btn>
      </v-list-item>

      <div v-if="user">
        <v-list-item class="height-90">
          <v-list-item-avatar>
            <v-img src="../../assets/person-blue.png"></v-img>
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title>이혜희</v-list-item-title>
          </v-list-item-content>
          <v-btn icon style="display: inline-block;">
            <v-icon>mdi-chevron-right</v-icon>
          </v-btn>
        </v-list-item>

        <v-divider></v-divider>
        <v-row class="text-center">
          <v-col
            cols="6"
            class="border-right pl-6"
          >
            <p class="mb-0">찜한가게</p>
          </v-col>
          <v-col
            cols="6"
            class="pr-6"
          >
            <p class="mb-0">리뷰관리</p>
          </v-col>
        </v-row>
      </div>
      <div v-else>
        <v-list-item class="height-90">
          <v-list-item-content>
            <v-list-item-title
              @click="goTo('auth')"
              class="primary-text">로그인</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </div>

      <v-divider></v-divider>
      <v-list dense>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
        >
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import router from '../../router'

export default {
  data () {
    return {
      drawer: false,
      items: [
        { title: '공지사항' },
        { title: '1:1문의' }
      ]
    }
  },
  computed: {
    ...mapState({
      toggleNavDrawer: state => state.toggle.navDrawerShow
    }),
    // 백엔드 연결하면 수정할 것
    ...mapState({
      user: state => state.toggle.tempUserInfoShow
    })
  },
  methods: {
    goTo (path) {
      this.drawer = false
      router.push({ name: path })
    }
  }
}
</script>

<style scoped>
.weight-700 {
  font-weight: 700;
}
.height-90 {
  height: 90px;
}
.border-right {
  border-right: 1px solid rgba(0, 0, 0, 0.12);
}
.primary-text {
  color: #005b8f;
}
</style>
