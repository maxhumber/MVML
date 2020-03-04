### Custom Domains (Heroku)

Follow this updated online tutorial: [link](https://www.namecheap.com/support/knowledgebase/article.aspx/9737/2208/pointing-a-domain-to-the-heroku-app)

**On Heroku** (in App Settings):

| Domain Name     | DNS Target                          |
| --------------- | ----------------------------------- |
| example.xyz     | word1-word2-0z0z0z0z0.herokudns.com |
| www.example.xyz | word3-word4-a9a9a9a9.herokudns.com  |

**On Namecheap** (in Advanced DNS):

Host Records              

| Type         | Host | Value                                | TTL       |
| ------------ | ---- | ------------------------------------ | --------- |
| ALIAS Record | @    | word1-word2-0z0z0z0z0.herokudns.com. | 5 min     |
| CNAME Record | www  | word3-word4-a9a9a9a9.herokudns.com.  | Automatic |


### Custom Domain (Docker)

**On Namecheap**

0. Buy a domain from namecheap (tip `.xyz` is dirt cheap!)

1. Sign in to your Namecheap account, then click **Domain List** in the left-hand column. You will be presented with a dashboard listing all of your domains. Click the **Manage** button of the domain you’d like to update:

![Namecheap domain dashboard entry](https://assets.digitalocean.com/articles/point_to_nameservers/namecheap-domain-list.png)

2. In the **Nameservers** section of the resulting screen, select **Custom DNS** from the dropdown menu and enter the following nameservers:

- ns1.digitalocean.com
- ns2.digitalocean.com
- ns3.digitalocean.com

![Namecheap custom dns nameserver entry](https://assets.digitalocean.com/articles/point_to_nameservers/namecheap-ns-entries.png)

3. Click the green checkmark to apply your changes. Now you are ready to move on to connecting the domain with your Droplet in the DigitalOcean control panel. Check out the Conclusion section at the end of this article to read on what to do next.

**On Digital Ocean**

1. From the [control panel](https://cloud.digitalocean.com), click **Create** in the top right, then click **Domains/DNS**.

2. In the **Enter Domain** section, enter the domain name.

   This is typically the apex domain, such as `example.com`. To add subdomains, like `www.example.com` or `images.example.com`, create DNS records for them after you add the apex domain.

3. Click **Add Domain**. This takes you to the **Create new record** page and adds NS records for the domain on DigitalOcean's name servers.

4. On the **Create new record** page, [add any DNS records](https://www.digitalocean.com/docs/networking/dns/how-to/manage-records/) for the domain. For each record, select the record type, fill in the necessary data, and click **Create Record**.

5. Sample records:

| Type  | Hostname        | Value                      | TTL (seconds) |      |
| ----- | --------------- | -------------------------- | ------------- | ---- |
| CNAME | www.example.xyz | is an alias of example.xyz | 43200         | More |
| A     | example.xyz     | directs to 142.93.XXX.104  | 3600          | More |
