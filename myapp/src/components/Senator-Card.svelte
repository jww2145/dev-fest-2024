/**
* This component will be rendered upon a senator bubble being clicked on. 
*
* @authors Joshua Wu
*/
<script>
    import ProgressBar from "./senate-charts/Progress-Bar.svelte";
    export let senator = null;
    export let progress = null;
</script>

{#if senator}
<div class="senator-card">
    <h2>{senator.name.official_full} </h2>
    <p><strong>State:</strong> {senator.state} - {senator.party}</p>
    <p><strong>Office:</strong> {senator.office}</p>
    <p><strong>Phone:</strong> <a href="tel:{senator.phone}">{senator.phone}</a></p>
    <p><strong>Contact:</strong> <a href="{senator.contact_form}" target="_blank">Contact Form</a></p>
    <p><strong>Term:</strong> {senator.start} to {senator.end}</p>
    <p><strong>Website:</strong> <a href="{senator.url}" target="_blank">{senator.url}</a></p>
    <p><strong>RSS Feed:</strong> <a href="{senator.rss_url}" target="_blank">RSS</a></p>
    <ProgressBar progress = {progress}/>
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
    .senator-card {
        padding: 20px;
        margin: 10px 0;
        border-radius: 8px;
    }
    .senator-card h2 {
        color: #333;
    }
    .senator-card a {
        color: #0066cc;
        text-decoration: none;
    }
    .senator-card a:hover {
        text-decoration: underline;
    }

    p{
        line-height:150%;
    }
</style>