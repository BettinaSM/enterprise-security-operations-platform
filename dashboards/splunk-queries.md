# Splunk Detection Queries

## SSH Failures

```spl
index=security "Failed password"
```

## Container Shell Detection

```spl
index=kubernetes "Shell spawned inside container"
```
