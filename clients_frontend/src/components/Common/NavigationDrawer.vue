<template>
  <div>
    <v-navigation-drawer
      :value="drawer"
      app
      temporary
      width="100%"
    >
      <v-list-item>
        <v-btn
          icon
          @click="turnoffDrawer"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
        <v-spacer></v-spacer>
				<div v-if="user">
					<v-btn 
						icon
						class="mx-3"
					>
						<v-icon>mdi-bell-outline</v-icon>
					</v-btn>
				</div>
				<div>
					<v-btn
						@click="goTo('main')"
						icon
					>
						<v-icon>mdi-home-outline</v-icon>
					</v-btn>
				</div>
      </v-list-item>

      <div v-if="user">
        <v-list-item class="height-90">
          <v-list-item-avatar>
            <v-img src="../../assets/person-blue.png"></v-img>
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title>이혜희</v-list-item-title>
          </v-list-item-content>
          <v-btn 
						@click="goTo('profile')"
						icon 
						class="right-btn"
					>
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
						@click="goTo('reviews')"
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
          @click="goTo(item.path)"
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
import { mapState, mapMutations } from 'vuex'
import router from '../../router'

export default {
  data () {
    return {
      items: [
        { title: '공지사항', path: 'main' },
        { title: '위치기반서비스 이용약관', path: 'termsofuse' },
        { title: '1:1문의', path: 'main' }
      ]
    }
  },
  computed: {
		// 백엔드 연결하면 수정할 것
    ...mapState({
			user: state => state.toggle.tempUserInfoShow,
			drawer: state => state.toggle.navDrawerShow,
    })
  },
  methods: {
		...mapMutations('toggle', ['toggleNavDrawer']),
    goTo (path) {
      this.toggleNavDrawer(false)
      router.push({ name: path })
		},
		turnoffDrawer() {
			this.toggleNavDrawer(false)
		}
  }
}
</script>

<style scoped>
.nav-fixed {
	/* display: absolute;
	height: 100vh; */
}
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
.right-btn {
	display: inline-block;
}
</style>
