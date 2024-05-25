#!/bin/bash

# Function to search for leaked credentials using regex
search_credentials() {
    local content=$(curl -s "$1")  # Fetch content of the webpage
    if [[ $? -ne 0 ]]; then
        echo "Failed to fetch URL: $1"
        exit 1
    fi

    echo "Searching for leaked credentials in $1..."
    echo "$content" | grep -Pio "(?i)((access_key|access_token|admin_pass|admin_user|algolia_admin_key|algolia_api_key|alias_pass|alicloud_access_key|amazon_secret_access_key|amazonaws|ansible_vault_password|aos_key|api_key|api_key_secret|api_key_sid|api_secret|api.googlemaps AIza|apidocs|apikey|apiSecret|app_debug|app_id|app_key|app_log_level|app_secret|appkey|appkeysecret|application_key|appsecret|appspot|auth_token|authorizationToken|authsecret|aws_access|aws_access_key_id|aws_bucket|aws_key|aws_secret|aws_secret_key|aws_token|AWSSecretKey|b2_app_key|bashrc password|bintray_apikey|bintray_gpg_password|bintray_key|bintraykey|bluemix_api_key|bluemix_pass|browserstack_access_key|bucket_password|bucketeer_aws_access_key_id|bucketeer_aws_secret_access_key|built_branch_deploy_key|bx_password|cache_driver|cache_s3_secret_key|cattle_access_key|cattle_secret_key|certificate_password|ci_deploy_password|client_secret|client_zpk_secret_key|clojars_password|cloud_api_key|cloud_watch_aws_access_key|cloudant_password|cloudflare_api_key|cloudflare_auth_key|cloudinary_api_secret|cloudinary_name|codecov_token|config|conn.login|connectionstring|consumer_key|consumer_secret|credentials|cypress_record_key|database_password|database_schema_test|datadog_api_key|datadog_app_key|db_password|db_server|db_username|dbpasswd|dbpassword|dbuser|deploy_password|digitalocean_ssh_key_body|digitalocean_ssh_key_ids|docker_hub_password|docker_key|docker_pass|docker_passwd|docker_password|dockerhub_password|dockerhubpassword|dot-files|dotfiles|droplet_travis_password|dynamoaccesskeyid|dynamosecretaccesskey|elastica_host|elastica_port|elasticsearch_password|encryption_key|encryption_password|env.heroku_api_key|env.sonatype_password|eureka.awssecretkey)[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"]([0-9a-zA-Z\-_=]{8,64})['\"]"
}

# Main function
main() {
    if [ $# -eq 0 ]; then
        echo "Usage: ./leaked_credentials_search.sh --url <url>"
        exit 1
    fi

    while [[ "$#" -gt 0 ]]; do
        case $1 in
            --url)
                url="$2"
                shift
                ;;
            *)
                echo "Unknown parameter passed: $1"
                echo "Usage: ./leaked_credentials_search.sh --url <url>"
                exit 1
                ;;
        esac
        shift
    done

    if [ -z "$url" ]; then
        echo "URL is required."
        echo "Usage: ./leaked_credentials_search.sh --url <url>"
        exit 1
    fi

    search_credentials "$url"
}

# Run the main function with provided arguments
main "$@"
