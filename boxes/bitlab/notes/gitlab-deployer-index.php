

<?php $input = file_get_contents("php://input");
	$payload  = json_decode($input); 
	$repo = $payload->project->name ?? '';
	$event = $payload->event_type ?? '';
	$state = $payload->object_attributes->state ?? '';
	$branch = $payload->object_attributes->target_branch ?? ''; 
	if ($repo=='Profile' && $branch=='master' && $event=='merge_request' && $state=='merged') {
     		echo shell_exec('cd ../profile/; sudo git pull'),"\n"; 
	} 
echo "OK\n";


