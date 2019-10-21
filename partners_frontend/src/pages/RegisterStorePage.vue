<template>
  <v-col>
    <div cols="12" class="register-head mb-4">영업장 등록</div>
    <div>
      <v-text-field
        label="사업자 성명"
        v-model="partnerName"
        :error-messages="partnerNameErrors"
        @input="$v.partnerName.$touch()"
        @blur="$v.partnerName.$touch()"
        required
        outlined
        rounded
        clearable
        autocomplete="off"
      ></v-text-field>
      <v-text-field
        label="상호명"
        v-model="storeName"
        :error-messages="storeNameErrors"
        @input="$v.storeName.$touch()"
        @blur="$v.storeName.$touch()"
        required
        outlined
        rounded
        clearable
        autocomplete="off"
      ></v-text-field>
      <v-text-field
        label="사업장 주소"
        v-model="address"
        :error-messages="addressErrors"
        @input="$v.address.$touch()"
        @blur="$v.address.$touch()"
        required
        outlined
        rounded
        clearable
        autocomplete="off"
      ></v-text-field>
      <v-text-field
        label="사업 등록번호"
        v-model="regiNumber"
        :error-messages="regiNumberErrors"
        @input="$v.regiNumber.$touch()"
        @blur="$v.regiNumber.$touch()"
        required
        outlined
        rounded
        clearable
        autocomplete="off"
      ></v-text-field>
      <v-file-input class="mt-0" label="사업자 등록증을 첨부하세요."></v-file-input>
    </div>
    <v-col class="center pt-4" cols="12">
      <v-btn class="Noto-Sans-KR" x-large color="primary">나의 사업장 요청하기</v-btn>
    </v-col>
    <v-row>
      <v-col class="Noto-Sans-KR center-also-align bottom-position fill-width">
        <v-icon>fas fa-exclamation</v-icon><span class="pl-2 footer-text">사업장 요청 후 영업일 기준 하루가 소요됩니다.</span>
      </v-col>
    </v-row>
  </v-col>
</template>

<script>
import { validationMixin } from 'vuelidate'
import { required, email, minLength, sameAs } from 'vuelidate/lib/validators'

export default {
  data () {
    return {
      storeName: '',
      partnerName: '',
      address: '',
      regiNumber: ''
    }
  },
  mixins: [validationMixin],
  validations: {
    storeName: {
      required
    },
    partnerName: {
      required
    },
    address: {
      required
    },
    regiNumber: {
      required
    }
  },
  computed: {
    storeNameErrors () {
      const errors = []
      if (!this.$v.storeName.$dirty) {
        return errors
      };
      !this.$v.storeName.required && errors.push('상호명을 입력해주세요.')
      return errors
    },
    partnerNameErrors () {
      const errors = []
      if (!this.$v.partnerName.$dirty) {
        return errors
      };
      !this.$v.partnerName.required && errors.push('사업자 성명을 입력해주세요.')
      return errors
    },
    addressErrors () {
      const errors = []
      if (!this.$v.address.$dirty) {
        return errors
      };
      !this.$v.address.required && errors.push('사업장 주소를 입력해주세요.')
      return errors
    },
    regiNumberErrors () {
      const errors = []
      if (!this.$v.regiNumber.$dirty) {
        return errors
      };
      !this.$v.regiNumber.required && errors.push('사업 등록번호를 입력해주세요.')
      return errors
    }
  }
}
</script>

<style scoped>
.register-head {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 60px;
  font-weight: 900;
}
.register-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 20px;
  font-weight: 900;
}
.text-area-font {
  font-family: 'Noto Sans KR', sans-serif;
}
.center {
  display: flex;
  justify-content: center;
}
.Noto-Sans-KR {
  font-family: 'Noto Sans KR', sans-serif;
}
.center-also-align {
  display: flex;
  justify-content: center;
  align-items: center;
}
.bottom-position {
  position: absolute;
  bottom: 12px;
}
.footer-text {
  font-family: 'Noto Sans KR', sans-serif;
  color: #7b7b7b;
}
</style>