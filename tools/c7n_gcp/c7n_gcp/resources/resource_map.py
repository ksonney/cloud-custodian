# Copyright The Cloud Custodian Authors.
ResourceMap = {
    "gcp.api-key": "c7n_gcp.resources.iam.ApiKey",
    "gcp.app-engine": "c7n_gcp.resources.appengine.AppEngineApp",
    "gcp.app-engine-certificate": "c7n_gcp.resources.appengine.AppEngineCertificate",
    "gcp.app-engine-domain": "c7n_gcp.resources.appengine.AppEngineDomain",
    "gcp.app-engine-domain-mapping": "c7n_gcp.resources.appengine.AppEngineDomainMapping",
    "gcp.app-engine-firewall-ingress-rule": (
        "c7n_gcp.resources.appengine.AppEngineFirewallIngressRule"),
    "gcp.app-engine-service": "c7n_gcp.resources.appengine.AppEngineService",
    "gcp.app-engine-service-version": "c7n_gcp.resources.appengine.AppEngineServiceVersion",
    "gcp.artifact-repository": (
        "c7n_gcp.resources.artifactregistry.ArtifactRegistryRepository"),
    "gcp.autoscaler": "c7n_gcp.resources.compute.Autoscaler",
    "gcp.bigtable-instance": "c7n_gcp.resources.bigtable.BigTableInstance",
    "gcp.bigtable-instance-cluster": "c7n_gcp.resources.bigtable.BigTableInstanceCluster",
    "gcp.bigtable-instance-table": "c7n_gcp.resources.bigtable.BigTableInstanceTable",
    "gcp.bigtable-instance-cluster-backup":
        "c7n_gcp.resources.bigtable.BigTableInstanceClusterBackup",
    "gcp.bq-dataset": "c7n_gcp.resources.bigquery.DataSet",
    "gcp.bq-job": "c7n_gcp.resources.bigquery.BigQueryJob",
    "gcp.bq-table": "c7n_gcp.resources.bigquery.BigQueryTable",
    "gcp.bucket": "c7n_gcp.resources.storage.Bucket",
    "gcp.build": "c7n_gcp.resources.build.CloudBuild",
    "gcp.cloudbilling-account": "c7n_gcp.resources.cloudbilling.CloudBillingAccount",
    "gcp.cloud-run-service": "c7n_gcp.resources.cloudrun.CloudRunService",
    "gcp.cloud-run-job": "c7n_gcp.resources.cloudrun.CloudRunJob",
    "gcp.compute-project": "c7n_gcp.resources.compute.Project",
    "gcp.dataflow-job": "c7n_gcp.resources.dataflow.DataflowJob",
    "gcp.datafusion-instance": "c7n_gcp.resources.datafusion.DatafusionInstance",
    "gcp.disk": "c7n_gcp.resources.compute.Disk",
    "gcp.dm-deployment": "c7n_gcp.resources.deploymentmanager.DMDeployment",
    "gcp.dns-managed-zone": "c7n_gcp.resources.dns.DnsManagedZone",
    "gcp.dns-policy": "c7n_gcp.resources.dns.DnsPolicy",
    "gcp.firewall": "c7n_gcp.resources.network.Firewall",
    "gcp.folder": "c7n_gcp.resources.resourcemanager.Folder",
    "gcp.function": "c7n_gcp.resources.function.Function",
    "gcp.secret": "c7n_gcp.resources.secret.Secret",
    "gcp.gke-cluster": "c7n_gcp.resources.gke.KubernetesCluster",
    "gcp.gke-nodepool": "c7n_gcp.resources.gke.KubernetesClusterNodePool",
    "gcp.iam-role": "c7n_gcp.resources.iam.Role",
    "gcp.image": "c7n_gcp.resources.compute.Image",
    "gcp.instance": "c7n_gcp.resources.compute.Instance",
    "gcp.instance-template": "c7n_gcp.resources.compute.InstanceTemplate",
    "gcp.interconnect": "c7n_gcp.resources.network.Interconnect",
    "gcp.interconnect-attachment": "c7n_gcp.resources.network.InterconnectAttachment",
    "gcp.kms-cryptokey": "c7n_gcp.resources.kms.KmsCryptoKey",
    "gcp.kms-cryptokey-version": "c7n_gcp.resources.kms.KmsCryptoKeyVersion",
    "gcp.kms-keyring": "c7n_gcp.resources.kms.KmsKeyRing",
    "gcp.loadbalancer-address": "c7n_gcp.resources.loadbalancer.LoadBalancingAddress",
    "gcp.loadbalancer-backend-bucket": "c7n_gcp.resources.loadbalancer.LoadBalancingBackendBucket",
    "gcp.loadbalancer-backend-service": (
        "c7n_gcp.resources.loadbalancer.LoadBalancingBackendService"),
    "gcp.loadbalancer-forwarding-rule": (
        "c7n_gcp.resources.loadbalancer.LoadBalancingForwardingRule"),
    "gcp.loadbalancer-global-address": "c7n_gcp.resources.loadbalancer.LoadBalancingGlobalAddress",
    "gcp.loadbalancer-global-forwarding-rule": (
        "c7n_gcp.resources.loadbalancer.LoadBalancingGlobalForwardingRule"),
    "gcp.loadbalancer-health-check": "c7n_gcp.resources.loadbalancer.LoadBalancingHealthCheck",
    "gcp.loadbalancer-http-health-check": (
        "c7n_gcp.resources.loadbalancer.LoadBalancingHttpHealthCheck"),
    "gcp.loadbalancer-https-health-check": (
        "c7n_gcp.resources.loadbalancer.LoadBalancingHttpsHealthCheck"),
    "gcp.loadbalancer-ssl-certificate": (
        "c7n_gcp.resources.loadbalancer.LoadBalancingSslCertificate"),
    "gcp.loadbalancer-ssl-policy": "c7n_gcp.resources.loadbalancer.LoadBalancingSslPolicy",
    "gcp.loadbalancer-target-http-proxy": (
        "c7n_gcp.resources.loadbalancer.LoadBalancingTargetHttpProxy"),
    "gcp.loadbalancer-target-https-proxy": (
        "c7n_gcp.resources.loadbalancer.LoadBalancingTargetHttpsProxy"),
    "gcp.loadbalancer-target-instance": (
        "c7n_gcp.resources.loadbalancer.LoadBalancingTargetInstance"),
    "gcp.loadbalancer-target-pool": "c7n_gcp.resources.loadbalancer.LoadBalancingTargetPool",
    "gcp.loadbalancer-target-ssl-proxy": (
        "c7n_gcp.resources.loadbalancer.LoadBalancingTargetSslProxy"),
    "gcp.loadbalancer-target-tcp-proxy": (
        "c7n_gcp.resources.loadbalancer.LoadBalancingTargetTcpProxy"),
    "gcp.loadbalancer-url-map": "c7n_gcp.resources.loadbalancer.LoadBalancingUrlMap",
    "gcp.log-exclusion": "c7n_gcp.resources.logging.LogExclusion",
    "gcp.log-project-metric": "c7n_gcp.resources.logging.LogProjectMetric",
    "gcp.log-project-sink": "c7n_gcp.resources.logging.LogProjectSink",
    "gcp.ml-job": "c7n_gcp.resources.mlengine.MLJob",
    "gcp.ml-model": "c7n_gcp.resources.mlengine.MLModel",
    "gcp.organization": "c7n_gcp.resources.resourcemanager.Organization",
    "gcp.project": "c7n_gcp.resources.resourcemanager.Project",
    "gcp.project-role": "c7n_gcp.resources.iam.ProjectRole",
    "gcp.pubsub-snapshot": "c7n_gcp.resources.pubsub.PubSubSnapshot",
    "gcp.pubsub-subscription": "c7n_gcp.resources.pubsub.PubSubSubscription",
    "gcp.pubsub-topic": "c7n_gcp.resources.pubsub.PubSubTopic",
    "gcp.region": "c7n_gcp.region.Region",
    "gcp.route": "c7n_gcp.resources.network.Route",
    "gcp.router": "c7n_gcp.resources.network.Router",
    "gcp.service": "c7n_gcp.resources.service.Service",
    "gcp.service-account": "c7n_gcp.resources.iam.ServiceAccount",
    "gcp.service-account-key": "c7n_gcp.resources.iam.ServiceAccountKey",
    "gcp.snapshot": "c7n_gcp.resources.compute.Snapshot",
    "gcp.sourcerepo": "c7n_gcp.resources.source.SourceRepository",
    "gcp.spanner-database-instance": "c7n_gcp.resources.spanner.SpannerDatabaseInstance",
    "gcp.spanner-instance": "c7n_gcp.resources.spanner.SpannerInstance",
    "gcp.sql-backup-run": "c7n_gcp.resources.sql.SqlBackupRun",
    "gcp.sql-instance": "c7n_gcp.resources.sql.SqlInstance",
    "gcp.sql-ssl-cert": "c7n_gcp.resources.sql.SqlSslCert",
    "gcp.sql-user": "c7n_gcp.resources.sql.SqlUser",
    "gcp.subnet": "c7n_gcp.resources.network.Subnet",
    "gcp.vpc": "c7n_gcp.resources.network.Network",
}
# SPDX-License-Identifier: Apache-2.0
