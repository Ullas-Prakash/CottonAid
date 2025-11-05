$(document).ready( function() {
    // Hide all result sections initially
    $('#results-container').hide();
    $('#legacy-results').hide();
    $('#error-display').hide();
    $('#loading').hide();

    //image_preview 
    $(document).on('change', '.btn-file :file', function() {
        var input = $(this),
            label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
        input.trigger('fileselect', [label]);
    });

    $('.btn-file :file').on('fileselect', function(event, label) {
        var input = $(this).parents('.input-group').find(':text'),
            log = label;
        
        if( input.length ) {
            input.val(log);
        } else {
            if( log ) alert(log);
        }
    });

    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            
            reader.onload = function (e) {
                $('#img-upload').attr('src', e.target.result).addClass('show');
            }
            
            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#imgInp").change(function(){
        readURL(this);
        // Reset all displays
        $('#results-container').hide();
        $('#legacy-results').hide();
        $('#error-display').hide();
        
        // Smooth scroll to results area
        setTimeout(function() {
            $('html, body').animate({
                scrollTop: $("#Bottom").offset().top - 20
            }, 800);
        }, 100);
    }); 	

    // Enhanced Predict Function
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);
        
        // Show loading indicator
        $('#loading').show();
        $('#results-container').hide();
        $('#legacy-results').hide();
        $('#error-display').hide();
        
        // Make prediction by calling enhanced API
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            timeout: 30000, // 30 second timeout
            success: function (data) {
                $('#loading').hide();
                
                if (typeof data === 'object' && data.success) {
                    // Enhanced prediction result
                    displayEnhancedResults(data);
                } else if (typeof data === 'object' && data.error) {
                    // Show error from enhanced system
                    showError(data.error);
                } else if (typeof data === 'string') {
                    // Fallback to legacy display (original system)
                    displayLegacyResults(data);
                } else {
                    showError('Unknown response format');
                }
            },
            error: function(xhr, status, error) {
                $('#loading').hide();
                if (status === 'timeout') {
                    showError('Request timed out. Please try again.');
                } else {
                    showError('Network error: ' + error);
                }
            }
        });
    });

    function displayEnhancedResults(data) {
        const disease = data.disease_prediction;
        const pests = data.pest_predictions;
        const treatments = data.treatment_recommendations;
        
        // Disease Detection Results
        $('#primary-disease').text(disease.primary_disease);
        $('#disease-confidence').text((disease.confidence * 100).toFixed(1) + '%');
        
        // Set severity badge
        const severityBadge = $('#severity-level');
        severityBadge.removeClass('badge-success badge-warning badge-danger');
        if (disease.severity_level === 'high') {
            severityBadge.addClass('badge-danger').text('High');
        } else if (disease.severity_level === 'medium') {
            severityBadge.addClass('badge-warning').text('Medium');
        } else {
            severityBadge.addClass('badge-success').text('Low');
        }
        
        $('#disease-description').text(treatments.description || '');
        
        // Alternative predictions
        let altPredHtml = '';
        if (disease.all_predictions && disease.all_predictions.length > 1) {
            for (let i = 1; i < Math.min(4, disease.all_predictions.length); i++) {
                const pred = disease.all_predictions[i];
                altPredHtml += `<p><strong>${pred.disease}:</strong> ${(pred.confidence * 100).toFixed(1)}%</p>`;
            }
        }
        $('#alternative-predictions').html(altPredHtml);
        
        // Pest Predictions
        if (pests && pests.length > 0) {
            let pestHtml = '';
            pests.forEach(pest => {
                pestHtml += `
                    <div class="mb-3 p-3 border rounded">
                        <h5>${pest.pest_name} <small class="text-muted">(${pest.scientific_name})</small></h5>
                        <p><strong>Type:</strong> ${pest.pest_type} | <strong>Confidence:</strong> ${(pest.confidence * 100).toFixed(1)}%</p>
                        <p><strong>Damage:</strong> ${pest.damage_description}</p>
                        <p><strong>Lifecycle:</strong> ${pest.lifecycle_info}</p>
                    </div>
                `;
            });
            $('#pest-predictions').html(pestHtml);
            $('#pest-card').show();
        } else {
            $('#pest-card').hide();
        }
        
        // Treatment Recommendations
        const urgencyBadge = $('#urgency-level');
        urgencyBadge.removeClass('badge-success badge-warning badge-danger badge-dark');
        if (treatments.calculated_urgency === 'critical' || treatments.urgency === 'high') {
            urgencyBadge.addClass('badge-danger').text('High Priority');
        } else if (treatments.urgency === 'medium') {
            urgencyBadge.addClass('badge-warning').text('Medium Priority');
        } else if (treatments.urgency === 'low') {
            urgencyBadge.addClass('badge-success').text('Low Priority');
        } else {
            urgencyBadge.addClass('badge-dark').text('Monitor');
        }
        
        $('#action-required').text(treatments.application_timing?.immediate_action || 'Monitor plant health');
        
        // Chemical Treatments
        let chemicalHtml = '';
        if (treatments.chemical_treatments && treatments.chemical_treatments.length > 0) {
            treatments.chemical_treatments.forEach(treatment => {
                chemicalHtml += `
                    <div class="mb-3 p-3 border rounded">
                        <h5>${treatment.product}</h5>
                        <p><strong>Active Ingredient:</strong> ${treatment.active_ingredient}</p>
                        <p><strong>Dosage:</strong> ${treatment.dosage}</p>
                        <p><strong>Application:</strong> ${treatment.application}</p>
                        <p><strong>Timing:</strong> ${treatment.timing}</p>
                        <p class="text-warning"><strong>Precautions:</strong> ${treatment.precautions}</p>
                    </div>
                `;
            });
        } else {
            chemicalHtml = '<p class="text-muted">No chemical treatments recommended for this condition.</p>';
        }
        $('#chemical-treatments').html(chemicalHtml);
        
        // Organic Treatments
        let organicHtml = '';
        if (treatments.organic_treatments && treatments.organic_treatments.length > 0) {
            treatments.organic_treatments.forEach(treatment => {
                organicHtml += `
                    <div class="mb-3 p-3 border rounded">
                        <h5>${treatment.method}</h5>
                        <p><strong>Procedure:</strong> ${treatment.procedure}</p>
                        <p><strong>Timing:</strong> ${treatment.timing}</p>
                        <p><strong>Effectiveness:</strong> ${treatment.effectiveness}</p>
                    </div>
                `;
            });
        } else {
            organicHtml = '<p class="text-muted">No organic treatments available for this condition.</p>';
        }
        $('#organic-treatments').html(organicHtml);
        
        // Prevention Methods
        let preventionHtml = '';
        if (treatments.prevention && treatments.prevention.length > 0) {
            preventionHtml = '<ul>';
            treatments.prevention.forEach(method => {
                preventionHtml += `<li>${method}</li>`;
            });
            preventionHtml += '</ul>';
        } else {
            preventionHtml = '<p class="text-muted">Continue regular monitoring and good agricultural practices.</p>';
        }
        $('#prevention-methods').html(preventionHtml);
        
        // Show results
        $('#results-container').fadeIn(600);
    }

    function displayLegacyResults(data) {
        $('.result').text(data);
        
        // Show appropriate legacy section
        if(data == 'Fusarium Wilt'){
            $('.Fusarium').show();
            $('.Curl').hide();
            $('.HPlant').hide();
            $('.HLeaf').hide();
        }
        else if(data == 'Leaf Curl Disease'){
            $('.Curl').show();
            $('.Fusarium').hide();
            $('.HPlant').hide();
            $('.HLeaf').hide();
        }
        else if(data == 'Healthy Leaf'){
            $('.HLeaf').show();
            $('.Fusarium').hide();
            $('.HPlant').hide();
            $('.Curl').hide();
        }
        else if(data == 'Healthy Plant'){
            $('.HPlant').show();
            $('.Fusarium').hide();
            $('.Curl').hide();
            $('.HLeaf').hide();
        }
        
        $('#legacy-results').fadeIn(600);
    }

    function showError(message) {
        $('#error-message').text(message);
        $('#error-display').fadeIn(600);
    }
});