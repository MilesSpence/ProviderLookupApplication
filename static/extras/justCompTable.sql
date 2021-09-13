DROP TABLE IF EXISTS complete;
CREATE TABLE complete 
AS (SELECT 
	NPIData.NPI, taxonomy.Groupingc, taxonomy.Classification, taxonomy.Definition, 
	
	NPIData.ProviderFirstName, NPIData.ProviderLastNameLegalName, NPIData.AuthorizedOfficialFirstName, NPIData.AuthorizedOfficialLastName,
	
	NPIData.ProviderFirstLineBusinessMailingAddress, NPIData.ProviderBusinessMailingAddressCityName, NPIData.ProviderBusinessMailingAddressStateName, 
	NPIData.ProviderBusinessMailingAddressPostalCode, NPIData.ProviderBusinessMailingAddressFaxNumber, 

	NPIData.ProviderFirstLineBusinessPracticeLocationAddress, NPIData.ProviderBusinessPracticeLocationAddressCityName, NPIData.ProviderBusinessPracticeLocationAddressStateName, 
	NPIData.ProviderBusinessPracticeLocationAddressPostalCode, NPIData.ProviderBusinessPracticeLocationAddressCountryCodeIfoutsideUS, 

	NPIData.ProviderOrganizationNameLegalBusinessName, NPIData.ProviderGenderCode, NPIData.ProviderBusinessPracticeLocationAddressTelephoneNumber
FROM taxonomy INNER JOIN NPIData 
ON taxonomy.Code=NPIData.HealthcareProviderTaxonomyCode_1 WHERE NPIData.EntityTypeCode = '1'
);