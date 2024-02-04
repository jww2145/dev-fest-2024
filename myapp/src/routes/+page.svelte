<script>
    import Header from '../components/Header.svelte'
    import SenateChild from '../components/Senate-Child.svelte';
    import HouseChild from '../components/House-Child.svelte'
    import SenateCharts from '../components/Senate-Charts.svelte';

    
</script>

<Header />
<SenateChild/>
<HouseChild/>
<div class='buffer'></div>
<SenateCharts/>

<style>
    .buffer{
        padding: 5%;
    }
</style>