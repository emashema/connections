<template>
    <div
        :class="{shake: shake, bounce: bounce, clicked: $parent.selected.map(s => s.value).includes(value)}"
        class="cell text-uppercase font-weight-bold"
        @click="$emit('toggle')"
    >
        <span
            :style="style"
            class="text-uppercase mb-0 font-weight-bold cursor-pointer"
        >{{ value }}</span>
    </div>
</template>

<script>
export default {
    props: {
        "value": {
            type: String,
            required: true
        },
        "parent": {
            type: String,
            required: true
        }
    },
    data() {
        return {
            shake: false,
            bounce: false
        }
    },
    computed: {
        style() {
            return this.value.length > 10 ? 'font-size:xx-small' : (
                    this.value.length > 8 ? 'font-size:x-small' : (
                    this.value.length > 7 ? 'font-size:small' : ''))
        }
    }
}
</script>