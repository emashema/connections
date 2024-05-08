<template>
    <b-modal
        id="results-modal"
        hide-header
        hide-footer
    >
        <div class="text-center">
            <h2 class="font-weight-bold">{{message}}</h2>
            <p> Connections #{{ day_of_year }}</p>
            <b-container class="mini-cell-container">
                <b-row
                    v-for="(attempt, index) in attempts"
                    :key="index"
                    no-gutters
                    class="my-1"
                >
                    <b-col
                        v-for="(item, index) in attempt"
                        :key="index"
                    >
                        <div
                            class="mini-cell"
                            :class="'level-'+item.level"
                        >
                        </div>
                    </b-col>
                </b-row>
            </b-container>
            <h5 class="mt-4">NEXT PUZZLE IN</h5>
            <timer/>
        </div>
    </b-modal>
</template>

<script>
import Timer from './Timer.vue';

export default {
    components: {
        Timer
    },
    props: {
        "day_of_year": {
            type: Number,
            required: true
        },
        "message": {
            type: String,
            required: true
        },
        "attempts": {
            type: Array,
            required: true
        }
    }
}
</script>

<style>

</style>