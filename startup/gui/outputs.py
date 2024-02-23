import GafferScene
import IECore
import IECoreScene

with IECore.IgnoredExceptions( ImportError ) :

	# If Arnold isn't available for any reason, this will fail
	# and we won't add any unnecessary output definitions.
	import GafferArnold

# Define render directories

aov_render_dir= "${project:rootDirectory}/renders/${script:name}/AOV/%s/%s.####.exr"
deep_render_dir= "${project:rootDirectory}/renders/${script:name}/deep/%s.####.exr"

# Interative plugs
beauty_interactive_plugs = {
					"driverType" : "ClientDisplayDriver",
					"displayHost" : "localhost",
					"displayPort" : "${image:catalogue:port}",
					"remoteDisplayType" : "GafferImage::GafferDisplayDriver",
					"filter" : "blackman_harris",
					"width" : 3,
					"layerName": "" # Populated per output
                }

tech_interactive_plugs = {
					"driverType" : "ClientDisplayDriver",
					"displayHost" : "localhost",
					"displayPort" : "${image:catalogue:port}",
					"remoteDisplayType" : "GafferImage::GafferDisplayDriver",
					"filter" : "gaussian",
					"width" : 3,
					"layerName": "" # Populated per output
				}
	
# Batch render plugs
beauty_batch_plugs = {
					"filter" : "blackman_harris",
					"width" : 3,
					"layerName" : "",
					"half_precision" : True,
					"tiled" : False,
					"autocrop" : False,
					"compression" : "" # Populated per output
}

tech_batch_plugs = {
					"filter" : "gaussian",
					"width" : 3,
					"layerName" : "",
					"half_precision" : False,
					"tiled" : False,
					"autocrop" : False,
					"compression" : "zip"
}

cryptomatte_batch_plug = {
					"filter" : "blackman_harris",
					"width" : 3,
					"layerName" : "",
					"half_precision" : False,
					"tiled" : False,
					"autocrop" : False,
					"compression" : "zip"
}

deep_batch_plug = {
					"filter" : "blackman_harris",
					"width" : 3,
					"layerName" : "",
					"tiled" : False,
					"autocrop" : False,
					"subpixel_merge" : True,
					"alpha_tolerance" : 0.01,
					"depth_tolerance" : 0.01,
					"layer_tolerance" : 0.01,
					"alpha_half_precision" : True,
					"depth_half_precision" : False

			
}


# beauty outputs
beauty_outputs ={
					"beauty":"lpe C.*",

					"diffuse":"lpe C<RD>.*",
					"specular":"lpe C<RS[^'coat']>.*",
					"coat":"lpe C<RS'coat'>.*",
					"transmission":"lpe C<TS>.*",
					"sss":"lpe C<TS>.*",
					"sheen":"lpe C<RS'sheen'>.*",
					"volume":"CV.*",

					"diffuse_direct":"lpe C<RD>L",
					"specular_direct":"lpe C<RS[^'coat']>L",
					"coat_direct":"lpe C<RS'coat'>L",
					"transmission_direct":"lpe C<TS>L",
					"sss_direct":"lpe C<TD>L",
					"sheen_direct":"lpe C<RS'sheen'>L",
					"volume_direct":"lpe CVL",


					"diffuse_indirect":"lpe C<RD>[DSVOB].*",
					"specular_indirect":"lpe C<RS[^'coat']>[DSVOB].*",
					"coat_indirect":"lpe C<RS'coat'>[DSVOB].*",
					"transmission_indirect":"lpe C<TS>[DSVOB].*",
					"sss_indirect":"lpe C<TD>[DSVOB].*",
					"sheen_indirect":"lpe C<RS'sheen'>[DSVOB].*",
					"volume_indirect":"lpe CV[DSVOB].*",


					"diffuse_albedo":"lpe C<RD>A",
					"specular_albedo":"lpe C<RS[^'coat']>A",
					"coat_albedo":"lpe C<RS'coat'>A",
					"transmission_albedo":"lpe C<TS>A",
					"sss_albedo":"lpe C<TD>A",
					"sheen_albedo":"lpe C<RS'sheen'>A",
					"volume_albedo":"lpe CVA",

					"ambient_occlusion":"color ambient_occlusion"
				}

# Tech outputs
tech_outputs = {
		"Pref":"vector Pref",
        "N":"vector N",
		"P":"vector P",
		"uv":"color uv",
		"Z":"float Z",
		"motionvector" : "motionvector"
    }

# Cryptomatte outputs
cryptomatte_outputs = {
		"crypto_object" : "color crypto_object",
		"crypto_asset" : "color crypto_asset",
		"crypto_material" : "color crypto_material"
}

# Deep output
deep_outputs = {
		"deep" : "float A"
}

# lightgroup list
lightgroup_list= [
					'lightgroup_1',
					'lightgroup_2',
					'lightgroup_3',
					'lightgroup_4',
					'lightgroup_5',
					'lightgroup_6',
					'lightgroup_7',
					'lightgroup_8',
					'lightgroup_9',
					'lightgroup_10',
					'lightgroup_11',
					'lightgroup_12']


# per lightgroup AOVs
lightgroup_components = {
		"diffuse_direct":"lpe C<RD>[<L.'lightgroup'>]",
		"diffuse_indirect":"lpe C<RD>[DSVOB].*[<L.'lightgroup'>]",
		"specular_direct":"lpe C<RS[^'coat']>[<L.'lightgroup'>]",
		"specular_indirect":"lpe C<RS[^'coat']>[DSVOB].*[<L.'lightgroup'>]",
		"coat_direct":"lpe C<RS'coat'>[<L.'lightgroup'>]",
		"coat_indirect":"lpe C<RS'coat'>[DSVOB].*[<L.'lightgroup'>]",
		"transmission_direct":"lpe C<TS>[<L.'lightgroup'>]",
		"transmission_indirect":"lpe C<TS>[DSVOB].*[<L.'lightgroup'>]",
		"sss_direct":"lpe C<TD>[<L.'lightgroup'>]",
		"sss_indirect":"lpe C<TD>[DSVOB].*[<L.'lightgroup'>]",
		"coat_direct":"lpe C<RS'coat'>[<L.'lightgroup'>]",
		"coat_indirect":"lpe C<RS'coat'>[DSVOB].*[<L.'lightgroup'>]",
		"volume_direct":"lpe CV[<L.'lightgroup'>]",
		"volume_indirect":"lpe CV[DSVOB].*[<L.'lightgroup'>]"
	}

# Create lightgroups outputs
for lightgroup in lightgroup_list:
	label = lightgroup.replace( "_", " " ).title().replace( " ", "_" )


	# Create lightgroups outputs for interactive rendering
	beauty_interactive_plugs["layerName"] = lightgroup
	GafferScene.Outputs.registerOutput(
		"RND/Interactive/Lightgroups/" + label,
		IECoreScene.Output(
			lightgroup,
			"ieDisplay",
			"lpe " + "C.*[<L.'%s'>V]" %(lightgroup),
			beauty_interactive_plugs
		)
	)

	# Create lightgroups outputs for batch rendering
	beauty_batch_plugs["layerName"] = lightgroup
	beauty_batch_plugs["compression"] = "dwaa"
	GafferScene.Outputs.registerOutput(
		"RND/Batch/Lightgroups/" + label,
		IECoreScene.Output(
			aov_render_dir % ( lightgroup, lightgroup ),
			"exr",
			"lpe " + "C.*[<L.'%s'>V]" %(lightgroup),
			beauty_batch_plugs
		)
	)
	
	# Create lightgroups components outputs
	for component in lightgroup_components.keys():
		component_label = label + "_" + component
		component_name = lightgroup + "_" + component
		data = lightgroup_components[component].replace("lightgroup", lightgroup)

	# Create lightgroups components outputs for interactive rendering
		beauty_interactive_plugs["layerName"] = component_name
		GafferScene.Outputs.registerOutput(
			"RND/Interactive/Lightgroups/" + lightgroup + "_" + "Components" + "/" + component_label,
			IECoreScene.Output(
				component_name,
				"ieDisplay",
				data,
				beauty_interactive_plugs
		)
	)
	# Create lightgroups components outputs for batch rendering
		beauty_batch_plugs["layerName"] = component_name
		beauty_batch_plugs["compression"] = "dwaa"
		GafferScene.Outputs.registerOutput(
			"RND/Batch/Lightgroups/" + lightgroup + "_" + "Components" + "/" + component_label,
			IECoreScene.Output(
				aov_render_dir % ( lightgroup, component_name ),
				"exr",
				data,
				beauty_batch_plugs
			)
		)


# Create tech AOVs outputs
for tech_aov in tech_outputs.keys():
	label = tech_aov.replace( "_", " " ).title().replace( " ", "_" )

	# Create tech AOVs outputs for interactive rendering
	tech_interactive_plugs["layerName"] = tech_aov
	GafferScene.Outputs.registerOutput(
		"RND/Interactive/Tech/" + label,
		IECoreScene.Output(
			tech_aov,
			"ieDisplay",
			tech_outputs[tech_aov],
			tech_interactive_plugs
		)
	)

	# Create tech AOVs outputs for batch rendering
	tech_batch_plugs["layerName"] = tech_aov
	GafferScene.Outputs.registerOutput(
		"RND/Batch/Tech/" + label,
		IECoreScene.Output(
			aov_render_dir % ( tech_aov, tech_aov ),
			"exr",
			tech_outputs[tech_aov],
			tech_batch_plugs
		)
	)

# Create beauty AOVs outputs
for beauty_aov in beauty_outputs.keys():
    label = beauty_aov.replace("_", " ").title().replace(" ", "_")

    # Create beauty AOVs outputs for interactive rendering
    if beauty_aov == "beauty":
        beauty_interactive_plugs["layerName"] = "RGBA"
    else:
        beauty_interactive_plugs["layerName"] = beauty_aov

    GafferScene.Outputs.registerOutput(
        "RND/Interactive/Beauty/" + label,
        IECoreScene.Output(
            beauty_aov,
            "ieDisplay",
            beauty_outputs[beauty_aov],
            beauty_interactive_plugs
        )
    )

    # Create beauty AOVs outputs for batch rendering
    if beauty_aov == "beauty":
        beauty_batch_plugs["layerName"] = "RGBA"
        beauty_batch_plugs["compression"] = "zip"
    else:
        beauty_batch_plugs["layerName"] = beauty_aov
        beauty_batch_plugs["compression"] = "dwaa"

    GafferScene.Outputs.registerOutput(
        "RND/Batch/Beauty/" + label,
        IECoreScene.Output(
            aov_render_dir % (beauty_aov, beauty_aov),
            "exr",
            beauty_outputs[beauty_aov],
            beauty_batch_plugs
        )
    )


	
# Create Cryptomatte AOVs outputs
for cryptomatte_aov	in cryptomatte_outputs.keys():
		label = cryptomatte_aov.replace( "_", " " ).title().replace( " ", "_" )

		# Create Cryptomatte AOVs outputs for batch rendering
		cryptomatte_batch_plug["layerName"] = cryptomatte_aov
		GafferScene.Outputs.registerOutput(
			"RND/Batch/Cryptomatte/" + label,
			IECoreScene.Output(
				aov_render_dir % ( "cryptomatte", cryptomatte_aov ),
				"exr",
				cryptomatte_outputs[cryptomatte_aov],
				cryptomatte_batch_plug
			)
		)

# Create DeepEXR output
for deep_aov in deep_outputs.keys():
		label = deep_aov.replace( "_", " " ).title().replace( " ", "_" )

		# Create DeepEXR output for batch rendering
		deep_batch_plug["layerName"] = ""
		GafferScene.Outputs.registerOutput(
			"RND/Batch/" + label,
			IECoreScene.Output(
			deep_render_dir % (deep_aov),
			"deepexr",
			deep_outputs[deep_aov],
			deep_batch_plug
			)
		)