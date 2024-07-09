<div id="message-text-3b4469f2-35c1-4a52-99f9-6408be00c0c5" class="markdown prose w-full flex flex-col break-words dark:prose-invert">
    <p>Certainly! Below is a formatted README in Markdown, which you can directly copy and paste into your GitHub repository's <a href="http://README.md">README.md</a> file:</p>

    <pre dir="ltr" class="w-full"><div class="dark bg-black mb-4 rounded-md">

<div class="p-4 overflow-y-auto">
<code id="code-content" class="!whitespace-pre hljs language-markdown">
<span class="hljs-section"># Django Studio Reservation System</span>

This project is a Django-based system that allows users to create accounts, authenticate, add studio details, and make reservations. It utilizes Docker to ensure easy setup and consistency across different environments.

<span class="hljs-section">## Features</span>

<span class="hljs-bullet">-</span> <span class="hljs-strong">**User Management**</span>: Create and manage user accounts.
<span class="hljs-bullet">-</span> <span class="hljs-strong">**Authentication**</span>: Obtain authentication tokens for API access.
<span class="hljs-bullet">-</span> <span class="hljs-strong">**Studio Management**</span>: Add and manage studio details.
<span class="hljs-bullet">-</span> <span class="hljs-strong">**Reservations**</span>: Users can make reservations for studios.

<span class="hljs-section">## Prerequisites</span>

Before you begin, ensure you have Docker and Docker Compose installed on your machine:
<span class="hljs-bullet">-</span> [<span class="hljs-string">Get Docker</span>](<span class="hljs-link">https://docs.docker.com/get-docker/</span>)
<span class="hljs-bullet">-</span> [<span class="hljs-string">Get Docker Compose</span>](<span class="hljs-link">https://docs.docker.com/compose/install/</span>)

<span class="hljs-section">## Setup and Installation</span>

<span class="hljs-bullet">1.</span> <span class="hljs-strong">**Clone the Repository**</span>
   <span class="hljs-code">```bash
   git clone https://your-repository-url.git
   cd your-project-directory
</span>
</code>
</div>
</div>
</pre>
<ol start="2">
<li>
<p>
<strong>Build the Docker Containers</strong>
</p>
<pre dir="ltr" class="w-full"><div class="dark bg-black mb-4 rounded-md">

<div class="p-4 overflow-y-auto">
<code id="code-content" class="!whitespace-pre hljs language-bash">docker-compose build
</code>
</div>
</div>
</pre>
</li>
<li>
<p>
<strong>Run the Containers</strong>
</p>
<pre dir="ltr" class="w-full"><div class="dark bg-black mb-4 rounded-md">

<div class="p-4 overflow-y-auto">
<code id="code-content" class="!whitespace-pre hljs language-bash">docker-compose up
</code>
</div>
</div>
</pre>
<p>This command will start all the services defined in your <code>docker-compose.yml</code>, including your Django application and any databases.</p>
</li>
</ol>
<h2>Using the API</h2>
<p>Once the application is running, you can use the following endpoints to interact with the system:</p>
<h3>Create a User</h3>
<ul>
<li>
<strong>Endpoint</strong>: <code>POST /users/</code>
</li>
<li>
<strong>Data</strong>:<pre dir="ltr" class="w-full"><div class="dark bg-black mb-4 rounded-md">

<div class="p-4 overflow-y-auto">
<code id="code-content" class="!whitespace-pre hljs language-json">
<span class="hljs-punctuation">{</span>
  <span class="hljs-attr">"username"</span>
<span class="hljs-punctuation">:</span> <span class="hljs-string">"newuser"</span>
<span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"password"</span>
<span class="hljs-punctuation">:</span> <span class="hljs-string">"newpassword"</span>
<span class="hljs-punctuation">}</span>
</code>
</div>
</div>
</pre>
</li>
</ul>
<h3>Obtain a Token</h3>
<ul>
<li>
<strong>Endpoint</strong>: <code>POST /api-token-auth/</code>
</li>
<li>
<strong>Data</strong>:<pre dir="ltr" class="w-full"><div class="dark bg-black mb-4 rounded-md">

<div class="p-4 overflow-y-auto">
<code id="code-content" class="!whitespace-pre hljs language-json">
<span class="hljs-punctuation">{</span>
  <span class="hljs-attr">"username"</span>
<span class="hljs-punctuation">:</span> <span class="hljs-string">"newuser"</span>
<span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"password"</span>
<span class="hljs-punctuation">:</span> <span class="hljs-string">"newpassword"</span>
<span class="hljs-punctuation">}</span>
</code>
</div>
</div>
</pre>
</li>
</ul>
<h3>Add a Studio</h3>
<ul>
<li>
<strong>Endpoint</strong>: <code>POST /studios/</code>
</li>
<li>
<strong>Header</strong>: <code>Authorization: Token &lt;Your_Token&gt;</code>
</li>
<li>
<strong>Data</strong>:<pre dir="ltr" class="w-full"><div class="dark bg-black mb-4 rounded-md">

<div class="p-4 overflow-y-auto">
<code id="code-content" class="!whitespace-pre hljs language-json">
<span class="hljs-punctuation">{</span>
  <span class="hljs-attr">"name"</span>
<span class="hljs-punctuation">:</span> <span class="hljs-string">"New Studio"</span>
<span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"location"</span>
<span class="hljs-punctuation">:</span> <span class="hljs-string">"Some Location"</span>
<span class="hljs-punctuation">}</span>
</code>
</div>
</div>
</pre>
</li>
</ul>
<h3>Make a Reservation</h3>
<ul>
<li>
<strong>Endpoint</strong>: <code>POST /reservations/</code>
</li>
<li>
<strong>Header</strong>: <code>Authorization: Token &lt;Your_Token&gt;</code>
</li>
<li>
<strong>Data</strong>:<pre dir="ltr" class="w-full"><div class="dark bg-black mb-4 rounded-md">

<div class="p-4 overflow-y-auto">
<code id="code-content" class="!whitespace-pre hljs language-json">
<span class="hljs-punctuation">{</span>
  <span class="hljs-attr">"studio"</span>
<span class="hljs-punctuation">:</span> studio_id<span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"date"</span>
<span class="hljs-punctuation">:</span> <span class="hljs-string">"2024-07-10"</span>
<span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"start_time"</span>
<span class="hljs-punctuation">:</span> <span class="hljs-string">"12:00"</span>
<span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"end_time"</span>
<span class="hljs-punctuation">:</span> <span class="hljs-string">"14:00"</span>
<span class="hljs-punctuation">}</span>
</code>
</div>
</div>
</pre>
</li>
</ul>
<h2>Managing the Application</h2>
<p>To manage your application, use the following Docker Compose commands:</p>
<ul>
<li>
<p>
<strong>Stopping Containers</strong>:</p>
<pre dir="ltr" class="w-full"><div class="dark bg-black mb-4 rounded-md">

<div class="p-4 overflow-y-auto">
<code id="code-content" class="!whitespace-pre hljs language-bash">docker-compose down
</code>
</div>
</div>
</pre>
</li>
<li>
<p>
<strong>Viewing Logs</strong>:</p>
<pre dir="ltr" class="w-full"><div class="dark bg-black mb-4 rounded-md">

<div class="p-4 overflow-y-auto">
<code id="code-content" class="!whitespace-pre hljs language-bash">docker-compose logs
</code>
</div>
</div>
</pre>
</li>
</ul>
<h2>Troubleshooting</h2>
<ul>
<li>
<strong>Container not starting</strong>: Check Docker logs for any errors during startup.</li>
<li>
<strong>Database issues</strong>: Ensure the database configuration in <code>docker-compose.yml</code> matches your Django settings.</li>
</ul>
<h2>Further Help</h2>
<p>For more information on Docker, visit the <a href="https://docs.docker.com/">Docker documentation</a>. For Django-related queries, refer to the <a href="https://docs.djangoproject.com/en/3.1/">Django documentation</a>.</p>
<pre dir="ltr" class="w-full"><div class="dark bg-black mb-4 rounded-md">

<div class="p-4 overflow-y-auto">
<code id="code-content" class="!whitespace-pre hljs language-">
This Markdown format is suitable for a GitHub README file, providing clear sections and code blocks for easy reading and understanding. Adjust the repository URL and any specific instructions as necessary for your project.</code>
</div>
</div>
</pre>
</div>
