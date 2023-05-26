<template>
  <div>
    <ProfileItem
    :id="id"
    />
  </div>
</template>

<script>
import ProfileItem from '@/components/ProfileItem.vue'

export default {
  name: 'ProfileView',
  components: {
    ProfileItem,
  },
  computed: {
    id() {
      return this.$route.params.id
    }
  }
  // created(){
  //   this.getid()
    
  // },
  // methods: {
  //   getid() {
  //     const profileId = this.$route.params.id
  //     console.log('profileID:',profileId)
  //   }
  // }

}
</script>

<style>

</style>