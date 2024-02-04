/**
* This component will be rendered upon a representative bubble being clicked on. 
*
* @authors Joshua Wu
*/
<script>
    export let rep = null;
</script>

{#if rep}
<div class="rep-card">
    <h2>{rep.CONG_REP} </h2>
    <p><strong>State:</strong> {rep.STATE} {rep.CONG_DIST} - {rep.PARTY_AFF}</p>
</div>
{:else}
<h2>What is an environmental score?</h2>
<p>Every now and then, the senate will vote on pressing environmental issues relating to
    <b>Justice and Democracy</b>, <b>Air Quality</b>, <b>Drilling</b>, and so on. We have scraped information
    on every environmental vote, going back to 1971. 
    </p>

   <p> To calculate a Senator's environmental vote, we divided the total amount of <b>pro-environmental</b> votes
    by the number of <b>total</b> votes.
</p>
{/if}

<style>
    .rep-card {
        padding: 20px;
        margin: 10px 0;
        border-radius: 8px;
    }
    .rep-card h2 {
        color: #333;
    }

    p{
        line-height:150%;
    }
</style>